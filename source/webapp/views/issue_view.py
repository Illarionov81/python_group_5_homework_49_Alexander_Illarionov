from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.views.base_views import SearchView
from webapp.models import IssueTracker, Project
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import View, TemplateView, FormView, DetailView, CreateView


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



class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(IssueTracker, pk=pk)
        if request.method == 'GET':
            return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, pk):
        task = get_object_or_404(IssueTracker, pk=pk)
        project_pk = task.project.pk
        task.delete()
        return redirect("project_view", pk=project_pk)


def multi_delete(request):
    data = request.POST.getlist('id')
    IssueTracker.objects.filter(pk__in=data).delete()
    return redirect('index')


# class TaskCreateView(FormView):
#     template_name = 'task/task_create.html'
#     form_class = TaskForm
#
#     def form_valid(self, form):
#         self.task = form.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.task.pk})

class TaskCreateView(CreateView):
    model = IssueTracker
    template_name = 'task/task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(
            Project,
            pk=self.kwargs.get('pk'),
        )
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('project_view', pk=project.pk)


class TaskUpdateView(FormView):
    template_name = 'task/task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('initial')
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(IssueTracker, pk=pk)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

