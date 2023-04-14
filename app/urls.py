from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('products/all/', views.products, name='products'),
    path('products/my/', views.my_products, name='my_products'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:pid>/', views.view_product, name='view_product'),
    path('products/<int:pid>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:pid>/delete/', views.delete_product, name='delete_product'),
]