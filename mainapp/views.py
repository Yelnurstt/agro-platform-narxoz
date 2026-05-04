import requests  # <-- Добавлен импорт для работы с внешним API (Task 4)
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator

from .models import Category, Farmer, Tag, Product, Order, OrderItem, Review
from .forms import UserRegisterForm
from .serializers import (
    CategorySerializer, FarmerSerializer, TagSerializer,
    ProductSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
)


def home(request):
    # --- TASK 4: Получение данных из внешнего API (Погода в Алматы) ---
    weather_data = None
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=43.2567&longitude=76.9286&current_weather=true"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            current_weather = data.get('current_weather', {})

            weather_data = {
                'temperature': current_weather.get('temperature'),
                'windspeed': current_weather.get('windspeed'),
            }
    except Exception as e:
        print("Ошибка при получении погоды:", e)

    context = {'weather': weather_data}
    return render(request, 'mainapp/home.html', context)


def about(request):
    return render(request, 'mainapp/about.html')


def product_list(request):
    products_all = Product.objects.select_related('category', 'farmer').all().order_by('-created_at')

    # --- TASK 3: Пагинация ---
    paginator = Paginator(products_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'mainapp/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'mainapp/product_detail.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


# ==========================================
# REST API (Django REST Framework)
# ==========================================

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# API View
class ProductCustomAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==========================================
# TASK 1: Регистрация и Авторизация
# ==========================================

# функция реги
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'mainapp/register.html', {'form': form})


# Класс ішкі входа
class UserLoginView(LoginView):
    template_name = 'mainapp/login.html'
    next_page = 'home'


# Класс выхода
class UserLogoutView(LogoutView):
    next_page = 'home'