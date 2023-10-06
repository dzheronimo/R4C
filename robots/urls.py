from django.urls import path, include

from .views import SummaryReport

urlpatterns = [
    path('report/', SummaryReport.as_view())
]