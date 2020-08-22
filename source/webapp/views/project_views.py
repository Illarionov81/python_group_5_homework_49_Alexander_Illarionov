from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from webapp.forms import SimpleSearchForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    context_object_name = 'projects_list'
    model = Project
    form = SimpleSearchForm
    paginate_by = 10
    paginate_orphans = 1



class OneProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    paginate_task_by = 5
    paginate_task_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        issues, page, is_paginated = self.paginate_comments(self.object)
        context['issues'] = issues
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_comments(self, project):
        issues = project.issue.all()
        if issues.count() > 0:
            paginator = Paginator(issues, self.paginate_task_by, orphans=self.paginate_task_orphans)
            page = paginator.get_page(self.request.GET.get('page', 1))
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return issues, None, False
