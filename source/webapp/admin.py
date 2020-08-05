from django.contrib import admin
from .models import IssueTracker, Status, Type


admin.site.register(IssueTracker)
admin.site.register(Status)
admin.site.register(Type)


