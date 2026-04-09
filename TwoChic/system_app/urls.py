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
    path('owner/employees/<int:pk>/delete/', views.delete_employee, name='delete_employee'),

    path('prodman/', views.prodman_homepage, name='prodman_homepage'),
    path('prodman_matinv/', views.prodman_matinv, name='prodman_matinv'),
    path('prodman/matinv/<int:pk>/edit/', views.edit_raw_material, name='edit_raw_material'),
    path('prodman/matinv/<int:pk>/delete/', views.delete_raw_material, name='delete_raw_material'),

    path('prodemp/home', views.prodemp_homepage, name='prodemp_home'),
    path('prod/matinv/', views.prod_matinv, name='prod_matinv'),
    
    path('prodemp/materials/', views.employee_materials, name='prodemp_matinv'),
    path('prodemp/products/', views.employee_products, name='prodemp_products_list'),
    
    path('prodman/products/', views.prodman_products, name='prodman_products_list'),

    path('owner/products/<int:pk>/', views.owner_product_detail, name='owner_product_detail'),
    path('prodman/products/<int:pk>/', views.prodman_product_detail, name='prodman_product_detail'),
    path('prodemp/products/<int:pk>/', views.prodemp_product_detail, name='prodemp_product_detail'),

    path('owner/product/<int:pk>/edit/', views.owner_edit_product, name='owner_edit_product'),
    path('owner/product/<int:pk>/delete/', views.owner_delete_product, name='owner_delete_product'),

    # API: Log Materials for Product
    path('api/products/<int:pk>/materials/', views.api_product_materials, name='api_product_materials'),
    path('api/products/<int:pk>/materials/<int:pm_pk>/', views.api_product_material_detail, name='api_product_material_detail'),
    path('api/raw-materials/', views.api_raw_materials_with_stock, name='api_raw_materials_with_stock'),
]

# Append new API URLs - need to patch the file
