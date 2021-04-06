from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Products
from accounts.models import User


def index(request):
    return HttpResponse("hello Shop")


class CreateProduct(LoginRequiredMixin, CreateView):
    model = Products
    fields = ['Product_Name', 'Price', 'Brand', 'Product_Image']
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct, self).form_valid(form)


class ProductList(LoginRequiredMixin, ListView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Products
    context_object_name = 'product'


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Products
    context_object_name = 'task'
    success_url = reverse_lazy('shop:product_list')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ['Product_Name', 'Price', 'Brand', 'Product_Image']
    success_url = reverse_lazy('shop:product_list')
