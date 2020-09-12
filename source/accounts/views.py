from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
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
    # paginate_related_by = 5
    # paginate_related_orphans = 0

    # def get_context_data(self, **kwargs):
    #     project = self.object.project
    #     paginator = Paginator(project, self.paginate_related_by, orphans=self.paginate_related_orphans)
    #     page_number = self.request.GET.get('page', 1)
    #     page = paginator.get_page(page_number)
    #     kwargs['page_obj'] = page
    #     kwargs['project'] = page.object_list
    #     kwargs['is_paginated'] = page.has_other_pages()
    #     return super().get_context_data(**kwargs)
