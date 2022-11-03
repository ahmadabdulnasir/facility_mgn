from django.urls import path
from .views import (
    SubmitReportView,
    ReportListView,
) 
urlpatterns = [
    path("report/add/", SubmitReportView.as_view(), name="report-add"),
    path("report/list/", ReportListView.as_view(), name="report-list"),
    path("report/details/<uid>/", ReportListView.as_view(), name="report-details"),
]
