from django.urls import path
from .views import (
    HomeView,
    UserLoginView,
    DashboardView,
    StudentDashboardView,
    # StudentAttendancedView,
    # AdmissionView,
    # AdmissionPrintView,
    # StaffDashboardView,
    # StudentProfileListView,
    # AdminEditStudent,
    # StudentSerialsListView,
    # StudentAttendanceListView,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("logout/", LogoutView.as_view(), {"next_page": "/"}, name="logout"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path(
        "dashboard/student/", StudentDashboardView.as_view(), name="student-dashboard"
    ),
    path("", HomeView.as_view()),
    # path("", UserLoginView.as_view()),
]
