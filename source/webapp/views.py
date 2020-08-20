from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.base_views import SearchView
from webapp.models import IssueTracker
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import View, TemplateView, FormView, ListView
from django.utils.http import urlencode


class TasksView(SearchView):
    template_name = 'index.html'
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


# class TasksView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'task_list'
#     model = IssueTracker
#     paginate_by = 10
#     paginate_orphans = 1
#
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['form'] = self.form
#         if self.search_value:
#             context['query'] = urlencode({'search': self.search_value})
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.search_value:
#             query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
#             queryset = queryset.filter(query)
#         return queryset
#
#     def get_search_form(self):
#         return SimpleSearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search']
#         return None


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


def multi_delete(request):
    data = request.POST.getlist('id')
    print(request.POST)
    print(data)
    IssueTracker.objects.filter(pk__in=data).delete()
    return redirect('index')


class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
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

