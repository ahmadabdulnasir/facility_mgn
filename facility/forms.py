from django import forms
from .models import Report
from facility_mgn.widgets import ImageWidget

class SubmitReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ("tracking_number", "actor", "status", "technician")
        widgets = {
            "photo": ImageWidget(),
            # "note": Textarea(attrs={"cols": 10, "rows": 3}),
        }

