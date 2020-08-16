from django.contrib import admin
from .models import IssueTracker, Status, Type


class IssueAdmin(admin.ModelAdmin):
    filter_horizontal = ('type',)
    list_filter = ('status',)
    list_display = ('pk', 'summary',)
    list_display_links = ('pk', 'summary')
    search_fields = ('type',)


admin.site.register(IssueTracker, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)


