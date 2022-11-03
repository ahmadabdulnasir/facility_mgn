from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
# Create your views here.


class HomeView(View):
    """ test view"""

    template_name = "accounts/login.html"
    context = {}

    def get(self, *args, **kwargs):
        self.context["extra_body_class"] = "login-page"
        return render(
            self.request, template_name=self.template_name, context=self.context
        )


class UserLoginView(View):
    """ Allows login of User"""

    template_name = "accounts/login.html"
    context = {}

    def post(self, *args, **kwargs):
        context = {}
        email = self.request.POST.get("email")
        password = self.request.POST.get("password")
        user = authenticate(self.request, email=email, password=password)
        if user and user.is_active:
            login(self.request, user)
            # Redirect to a success page.
            msg = "Login Success !!!"
            messages.add_message(
                self.request,
                messages.SUCCESS,
                message=msg,
            )
            return HttpResponseRedirect(reverse("accounts:dashboard"))
        msg = "Invalid Username and/or Password, Please Check and Try Again !!!"
        messages.add_message(
            self.request,
            messages.ERROR,
            message=msg,
        )
        return render(self.request, template_name=self.template_name, context=context)

    def get(self, *args, **kwargs):
        self.context["extra_body_class"] = "login-page"
        return render(
            self.request, template_name=self.template_name, context=self.context
        )



class DashboardView(LoginRequiredMixin, View):
    """ Allows managing of account fdashboar and redirect to the appropiate dashboard"""

    def get(self, *args, **kwargs):
        context = {}
        if self.request.user.user_type == "student":
            return HttpResponseRedirect(reverse("accounts:student-dashboard"))
        elif self.request.user.user_type == "staff":
            return HttpResponseRedirect(reverse("accounts:staff-dashboard"))
        elif self.request.user.user_type == "admin":
            return HttpResponseRedirect(reverse("accounts:staff-dashboard"))
        else:
            msg = "User not Allowed or User deactivated!!!"
            messages.add_message(
                self.request,
                messages.ERROR,
                message=msg,
            )
            return HttpResponseRedirect(reverse("accounts:logout"))

        return None


class StudentDashboardView(LoginRequiredMixin, View):
    """ Allows managing of account fdashboar and redirect to the appropiate dashboard"""
    template_name = "accounts/student/dashboard.html"
    def get(self, *args, **kwargs):
        user = self.request.user
        all_reports = user.faulty_reports.all()
        context = {
            "all_reports": all_reports,
            "total_reports": all_reports.count(),
            "treated_reports": all_reports.filter(status="treated").count(),
            "pending_reports": all_reports.filter(status="pending").count(),
            "rejected_reports": all_reports.filter(status="rejected").count(),
        }

        return render(
            self.request, template_name=self.template_name, context=context
        )
