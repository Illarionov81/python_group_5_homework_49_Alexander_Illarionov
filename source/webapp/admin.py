from django.contrib import admin
from .models import IssueTracker, Status, Type


class IssueAdmin(admin.ModelAdmin):
    filter_horizontal = ('type',)


admin.site.register(IssueTracker, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)


