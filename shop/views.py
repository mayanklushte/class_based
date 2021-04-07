from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Products
from accounts.models import User
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return HttpResponse("hello Shop")


class CreateProduct(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Products
    fields = ['Product_Name', 'Price', 'Brand', 'Product_Image']
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct, self).form_valid(form)

    def test_func(self):
        x = self.request.user
        if x.is_Shop:
            return True
        else:
            raise Http404("You are Nt Allowed here")


class ProductList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context

    def test_func(self):
        x = self.request.user
        if x.is_Shop:
            return True
        else:
            raise Http404("You are Nt Allowed here")


class ProductDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Products
    context_object_name = 'product'

    def test_func(self):
        x = self.request.user
        if x.is_Shop:
            return True
        else:
            raise Http404("You are Nt Allowed here")


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Products
    context_object_name = 'task'
    success_url = reverse_lazy('shop:product_list')

    def test_func(self):
        x = self.request.user
        if x.is_Shop:
            return True
        else:
            raise Http404("You are Nt Allowed here")


class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Products
    fields = ['Product_Name', 'Price', 'Brand', 'Product_Image']
    success_url = reverse_lazy('shop:product_list')

    def test_func(self):
        x = self.request.user
        if x.is_Shop:
            return True
        else:
            raise Http404("You are Nt Allowed here")
