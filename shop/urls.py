from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_product', views.CreateProduct.as_view(), name='create_product'),
    path('product_list', views.ProductList.as_view(), name='product_list'),
    path('product_detail/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('product_update/<int:pk>', views.ProductUpdate.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
