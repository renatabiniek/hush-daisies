"""URL paths for the Products app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_products, name='products'),
    path('<int:product_id>/', views.show_product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
