from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import IssueTracker
from webapp.forms import TaskForm, StatusForm, TypeForm
from django.views.generic import View, TemplateView


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


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
            return render(request, 'task_create.html', context={
                'form': TaskForm(),
                'form_status': StatusForm(),
                'form_type': TypeForm(),
            })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        form_status = StatusForm(data=request.POST)
        form_type = TypeForm(data=request.POST)
        if form.is_valid() and form_status.is_valid() and form_type.is_valid():
            summary = form.cleaned_data['summary']
            description = form.cleaned_data['description']
            status = form_status.cleaned_data['status']
            type = form_type.cleaned_data['type']
            task = IssueTracker.objects.create(summary=summary, description=description, status=status, type=type)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})


class TaskUpdateView(View):

    def get(self, request, pk):
        task = get_object_or_404(IssueTracker, pk=pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description
        })
        form_status = StatusForm(data={
            'status': task.status
        })
        form_type = TypeForm(data={
            'type': task.type
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task,
                                                            'form_status': form_status, 'form_type': form_type})

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(IssueTracker, pk=pk)
        form = TaskForm(data=request.POST)
        form_status = StatusForm(data=request.POST)
        form_type = TypeForm(data=request.POST)
        if form.is_valid() and form_status.is_valid() and form_type.is_valid():
            task.status = form_status.cleaned_data['status']
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.type = form_type.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_update.html', context={'task': task, 'form': form})
