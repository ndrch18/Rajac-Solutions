from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('login_view/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password_view, name='change_password'),

    path('owner/', views.owner_homepage, name='owner_homepage'),
    path('owner/employees/', views.owner_manage_employees, name='owner_manage_employees'),
    path('owner/products/', views.owner_products, name='owner_products'),
    path('owner/products/add/', views.owner_add_product, name='owner_add_product'),
    path('owner/products/list/', views.owner_products_list, name='owner_products_list'),

    path('prodman/', views.prodman_homepage, name='prodman_homepage'),
    path('prodman_matinv/', views.prodman_matinv, name='prodman_matinv'),
    path('prodman/matinv/<int:pk>/edit/', views.edit_raw_material, name='edit_raw_material'),
    path('prodman/matinv/<int:pk>/delete/', views.delete_raw_material, name='delete_raw_material'),

    path('prod/', views.prod_homepage, name='prod_homepage'),
    path('prod/matinv/', views.prod_matinv, name='prod_matinv'),
    path('prod/matinv/', views.prod_matinv, name='prod_matinv'),
]
