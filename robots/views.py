import datetime as dt
import pandas as pd
from io import BytesIO

from django.http import FileResponse
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


# def make_excel_from_data(data: dict):
#     df = pd.DataFrame(data)
#     today_date = dt.date.today()
#     timestamp = dt.datetime.now().timestamp()
#     file_name = f'summary_report_{today_date}_{timestamp}'
#     with pd.ExcelWriter(f'./{file_name}.xlsx') as writer:
#         temp_models = set(data['Модель'])
#
#         for model in temp_models:
#             df_sheet = df[df['Модель'] == model].groupby(['Модель', 'Версия']).sum()
#             df_sheet.to_excel(writer, sheet_name=f'{model}')
#     return f'{file_name}.xlsx'


def make_excel_from_data(data: dict):
    df = pd.DataFrame(data)
    today_date = dt.date.today()
    timestamp = dt.datetime.now().timestamp()
    file_name = f'summary_report_{today_date}_{timestamp}.xlsx'
    file_like_object = BytesIO()
    file_like_object.name = file_name
    file_like_object.encoding = 'utf-8'

    temp_models = sorted(set(data['Модель']))
    with pd.ExcelWriter(file_like_object) as file:
        for model in temp_models:
            df_sheet = df[df['Модель'] == model].groupby(['Модель', 'Версия']).sum()
            df_sheet.to_excel(file, sheet_name=f'{model}')
    file_like_object.seek(0)
    return file_like_object


class DownloadSummaryReport(View):

    def get(self, request):
        # if request.user.is_authenticated and request.user.role == 'director':
            report = make_summary_report()
            file = make_excel_from_data(report)
            return FileResponse(file, as_attachment=True)
        # Обработка в случае если пользователь не директор
        # ...

