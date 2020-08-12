from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import IssueTracker
from webapp.forms import TaskForm
from django.views.generic import View, TemplateView, FormView


class TasksView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_list = IssueTracker.objects.all()
        context['task_list'] = task_list
        return context


class OneTaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(IssueTracker, pk=pk)
        context['task'] = task
        return context


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(IssueTracker, pk=pk)
        if request.method == 'GET':
            return render(request, 'delete.html', context={'task': task})

    def post(self, request, pk):
        task = get_object_or_404(IssueTracker, pk=pk)
        task.delete()
        return redirect("index")


class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        data = {}
        type = form.cleaned_data.pop('type')
        for key, value in form.cleaned_data.items():
            if value is not None:
                data[key] = value
        self.task = IssueTracker.objects.create(**data)
        self.task.type.set(type)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status', 'type':
            initial[key] = getattr(self.task, key)
        initial['type'] = self.task.type.all()
        return initial

    def form_valid(self, form):
        type = form.cleaned_data.pop('type')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        self.task.type.set(type)
        return super().form_valid(form)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(IssueTracker, pk=pk)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

