from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-users-read/', views.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', views.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', views.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', views.UserDeleteView.as_view(), name='admin_users_delete'),
    path('categories/create/', views.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', views.categories, name='categories'),
    path('categories/update/<int:pk>/', views.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', views.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', views.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', views.products, name='products'),
    path('products/read/<int:pk>/', views.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
]
