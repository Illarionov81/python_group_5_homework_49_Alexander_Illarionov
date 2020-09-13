from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

from accounts.forms import MyUserCreationForm
from  django.views.generic import CreateView


# def login_view(request):
#     from_url = request.META.get('HTTP_REFERER', 'products')
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('projects')
#         else:
#             context['has_error'] = True
#     return render(request, 'registration/login.html', context=context)
#
# def logout_view(request):
#     from_url = request.META.get('HTTP_REFERER', 'products')
#     logout(request)
#     return redirect(from_url)
from webapp.models import Project


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_project_by = 5
    paginate_project_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        projects_list, page, is_paginated = self.paginate_comments(user)
        context['projects_list'] = projects_list
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_comments(self, user):
        project = user.project.filter(is_deleted=False).order_by('starts_date')
        if project.count() > 0:
            paginator = Paginator(project, self.paginate_project_by, orphans=self.paginate_project_orphans)
            page = paginator.get_page(self.request.GET.get('page', 1))
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return project, None, False


class AllUserView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'users_view.html'
    context_object_name = 'users_list'
    paginate_by = 5
    paginate_orphans = 1
    permission_required = "auth.view_user"


