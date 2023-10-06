import datetime as dt
import pandas as pd

from django.shortcuts import render
from django.utils import timezone
from django.views import View

from .models import Robot


def make_summary_report():
    # Указать timezone
    today = timezone.now()
    time_delta = dt.timedelta(days=7)
    week_limit = today - time_delta
    queryset = Robot.objects.filter(created__gte=week_limit)
    data = {'Модель': [],
            'Версия': [],
            'Количество за неделю': []
            }
    for robot in queryset:
        data['Модель'].append(robot.model)
        data['Версия'].append(robot.version)
        data['Количество за неделю'].append(1)

    return data


def make_excel_from_dataframe(data: dict):
    df = pd.DataFrame(data)
    today_date = dt.date.today()
    timestamp = dt.datetime.now().timestamp()
    file_name = f'summary_report_{today_date}_{timestamp}'
    with pd.ExcelWriter(f'./{file_name}.xlsx') as writer:
        temp_models = set(data['Модель'])

        for model in temp_models:
            df_sheet = df[df['Модель'] == model].groupby(['Модель', 'Версия']).sum()
            df_sheet.to_excel(writer, sheet_name=f'{model}')


class SummaryReport(View):
    def get(self, request):
        report = make_summary_report()
        make_excel_from_dataframe(report)

