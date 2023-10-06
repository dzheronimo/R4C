from django.urls import path, include

from .views import DownloadSummaryReport

urlpatterns = [
    path('report/', DownloadSummaryReport.as_view())
]