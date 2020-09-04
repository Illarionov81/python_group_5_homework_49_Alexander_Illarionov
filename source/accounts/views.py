from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import MyUserCreationForm


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

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})
