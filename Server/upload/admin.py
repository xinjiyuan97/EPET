from django.contrib import admin
from .models import UploadReport
# Register your models here.
class UploadReportAdmin(admin.ModelAdmin):
    list_display = ('owner', 'lessons', 'teacher')

admin.site.register(UploadReport, UploadReportAdmin)