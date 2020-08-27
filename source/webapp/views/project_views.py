from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SimpleSearchForm, ProjectForm
from webapp.models import Project


def multi_delete(request):
    data = request.POST.getlist('id')
    # Project.objects.filter(pk__in=data).delete()
    projects = Project.objects.filter(pk__in=data)
    for project in projects:
        project.is_deleted = True
        project.save()
    return redirect('projects')


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    context_object_name = 'projects_list'
    model = Project
    form = SimpleSearchForm
    paginate_by = 3
    paginate_orphans = 1

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     form = SimpleSearchForm(data=self.request.GET)
    #     if form.is_valid():
    #         search = form.cleaned_data['search']
    #         kwargs['search'] = search
    #     return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = self.model.objects.filter(is_deleted=False)
        # http://localhost:8000/?search=ygjkjhg
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return data.order_by('starts_date')


class OneProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    paginate_task_by = 5
    paginate_task_orphans = 0

    def get_queryset(self):
        data = self.model.objects.filter(is_deleted=False)
        return data

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


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/project_create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm

    def get_queryset(self):
        data = self.model.objects.filter(is_deleted=False)
        return data

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('projects')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        project = get_object_or_404(self.model, pk=self.object.pk)
        project.is_deleted = True
        project.save()
        return HttpResponseRedirect(success_url)


