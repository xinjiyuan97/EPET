from django.contrib import admin
from .models import Experiments, ContentOfClass
# Register your models here.
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('Title', 'expermentScore', 'belongs', 'owner', )

admin.site.register(Experiments, ExperimentAdmin)