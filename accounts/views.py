from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, authenticate
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
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            # Redirect to a success page.
            # if user.profile.user_type == "admin":
            return HttpResponseRedirect(reverse("accounts:dashboard"))
            # return HttpResponseRedirect("/")
        msg = "Invalid Username and/or Password, Please Check and Try Again !!!"
        messages.add_message(
            self.request,
            messages.ERROR,
            message=msg,
            extra_tags="text-danger bg-warning",
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
        # try:
        #     profile = UserProfile.objects.get(user=self.request.user)
        # except UserProfile.DoesNotExist:
        #     profile = False
        # if profile and profile.user_type == "student":
        #     return HttpResponseRedirect(reverse("accounts:student-dashboard"))
        # elif profile and profile.user_type == "staff":
        #     return HttpResponseRedirect(reverse("accounts:staff-dashboard"))
        # elif profile and profile.user_type == "admin":
        #     return HttpResponseRedirect(reverse("accounts:staff-dashboard"))
        # else:
        #     return HttpResponseRedirect(reverse("accounts:edit-profile"))

        return None