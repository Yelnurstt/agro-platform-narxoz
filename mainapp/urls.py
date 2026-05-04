from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# роутер генераций апи путей автоматом
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'farmers', views.FarmerViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    # HTML
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products_html/', views.product_list, name='product_list'),
    path('products_html/<int:product_id>/', views.product_detail, name='product_detail'),

    # маршруты API api
    path('api/', include(router.urls)),

    # Маршрут APIView
    path('api/custom-products/', views.ProductCustomAPIView.as_view(), name='custom_products_api'),
]
