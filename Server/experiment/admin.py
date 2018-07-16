from django.contrib import admin
from .models import Experiments, ContentOfClass
# Register your models here.
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'expermentScore', 'belongs', 'owner', )

class ContentOfClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', )

admin.site.register(Experiments, ExperimentAdmin)

admin.site.register(ContentOfClass, ContentOfClassAdmin)