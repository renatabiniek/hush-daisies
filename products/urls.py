from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_products, name='products'),
    path('<int:product_id>/', views.show_product_detail, name='product_detail'),
]
