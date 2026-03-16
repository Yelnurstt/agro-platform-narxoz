from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    # Task 8
    # CRUD для Прод
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    
    # CRUD для Категорий
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),

    # CRUD для Отзывов
    path('review/create/', views.ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review_delete'),
]