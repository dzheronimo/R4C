from django.urls import path

from .views import DownloadSummaryReport

urlpatterns = [
    path('report/', DownloadSummaryReport.as_view())
]
