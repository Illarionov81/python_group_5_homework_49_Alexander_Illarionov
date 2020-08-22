from django.contrib import admin
from .models import IssueTracker, Status, Type, Project


class IssueAdmin(admin.ModelAdmin):
    filter_horizontal = ('type',)
    list_filter = ('status',)
    list_display = ('pk', 'summary',)
    list_display_links = ('pk', 'summary')
    search_fields = ('type',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(IssueTracker, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project, ProjectAdmin)


