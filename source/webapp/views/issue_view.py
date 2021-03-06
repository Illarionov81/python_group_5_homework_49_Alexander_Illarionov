from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from webapp.views.base_views import SearchView
from webapp.models import IssueTracker, Project, Type
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import View, TemplateView, FormView, DetailView, CreateView, UpdateView, DeleteView


class TasksView(SearchView):
    template_name = 'task/index.html'
    context_object_name = 'task_list'
    model = IssueTracker
    paginate_by = 10
    paginate_orphans = 1
    form = SimpleSearchForm
    context = 'query'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset


class OneTaskView(DetailView):
    template_name = 'task/task.html'
    model = IssueTracker


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = IssueTracker
    template_name = 'task/delete.html'
    context_object_name = 'task'
    permission_required = 'webapp.delete_issuetracker'

    def get_success_url(self):
        return reverse("project_view", kwargs={'pk': self.object.project.pk})


@login_required
def multi_delete_task(request):
    data = request.POST.getlist('id')
    IssueTracker.objects.filter(pk__in=data).delete()
    return redirect('index')


class TaskCreateView(PermissionRequiredMixin, CreateView):
    model = IssueTracker
    template_name = 'task/task_create.html'
    form_class = TaskForm
    permission_required = 'webapp.add_issuetracker'

    def has_permission(self, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'),)
        try:
            user = project.users.get(pk=self.request.user.pk)
        except ObjectDoesNotExist:
            user = False
        return super().has_permission() and user

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'),)
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_view', pk=project.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs.get('pk'),)
        return context


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'task/task_update.html'
    form_class = TaskForm
    model = IssueTracker
    context_object_name = 'task'
    permission_required = 'webapp.change_issuetracker'

    def has_permission(self, **kwargs):
        task = get_object_or_404(IssueTracker, pk=self.kwargs.get('pk'),)
        project = task.project
        try:
            user = project.users.get(pk=self.request.user.pk)
        except ObjectDoesNotExist:
            user = False
        return super().has_permission() and user

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


