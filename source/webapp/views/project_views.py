from django.views.generic import ListView

from webapp.forms import SimpleSearchForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    context_object_name = 'projects_list'
    model = Project
    form = SimpleSearchForm
    paginate_by = 10
    paginate_orphans = 1