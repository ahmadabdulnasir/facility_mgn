from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse

from .forms import SubmitReportForm
# Create your views here.


class SubmitReportView(LoginRequiredMixin, View):
    """ Allows submission of Faulty Report by a Student"""
    template_name = "facility/report_add.html"

    def post(self, *args, **kwargs):
        context = {}
        form = SubmitReportForm(self.request.POST, self.request.FILES,)
        if form.is_valid():
            application = form.save(commit=False)
            application.actor = self.request.user
            application.save()
            msg = "Your Faulty Report was successfully submitted!"
            messages.add_message(
                request=self.request,
                level=messages.SUCCESS,
                message=msg,
            )
            return HttpResponseRedirect(reverse("facility:report-list"))
        else:
            msg = "Please correct the error below"
            messages.add_message(
                request=self.request,
                level=messages.ERROR,
                message=msg,
            )
            return render(request=self.request, template_name=self.template_name, context=locals())

    def get(self, *args, **kwargs):
        context = {}
        form = SubmitReportForm()
        context["form"] = form
        return render(request=self.request, template_name=self.template_name, context=context)


class ReportListView(LoginRequiredMixin, View):
    """ Show list of all report by a Student"""
    template_name = "facility/report_list.html"
    def get(self, *args, **kwargs):
        user = self.request.user
        all_reports = user.faulty_reports.all()
        context = {
            "all_reports": all_reports,
        }
        form = SubmitReportForm()
        context["form"] = form
        return render(request=self.request, template_name=self.template_name, context=context)
