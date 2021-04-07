from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'accounts/index.html', {})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form_r = form.save()
            form_r.is_customer = True
            form_r.set_password(form_r.password)
            form_r.save()
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/user_register.html', {'form': form})


def shop_register(request):
    if request.method == 'POST':
        form = ShopRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form_r = form.save()
            form_r.is_Shop = True
            form_r.set_password(form_r.password)
            form_r.save()
        else:
            print(form.errors)
    else:
        form = ShopRegisterForm()
    return render(request, 'accounts/Shop_register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_customer:
                login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            elif user.is_active and user.is_Shop:
                login(request, user)
                return HttpResponseRedirect(reverse('shop:index'))
            else:
                return HttpResponseRedirect(reverse('accounts:index'))
        else:
            print('user is not active')
    else:
        return render(request, 'accounts/admin_login.html')


