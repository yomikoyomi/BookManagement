from django.contrib import admin
from info.models import trn_infomation


class trn_infomationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_joined', 'date_updated', 'infomation_division')
    list_display_links = ('title', 'date_joined', 'date_updated', 'infomation_division')
admin.site.register(trn_infomation, trn_infomationAdmin)
