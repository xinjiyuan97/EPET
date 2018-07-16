from upload.models import UploadReport
from django import forms
from django.forms import widgets

class UploadReportForm(forms.Form):

    fillPath = forms.FileField(
        required = True,
        widget = widgets.FileInput(attrs = {'name': 'reportFile'}))
    lessons = forms.ChoiceField(label = "课程")
    remark = forms.CharField(
        required = False,
        max_length = 200,
        widget = widgets.TextInput(attrs = {'name':'remark', 'class': 'form-control1'}),)