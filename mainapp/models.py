from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# 1 Категории товаров
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Название категории"))
    description = models.TextField(blank=True, verbose_name=_("Описание"))

    def __str__(self):
        return self.name

# 2 Профиль фермера Связь One-to-One с базовым юзером Django
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    farm_name = models.CharField(max_length=200, verbose_name=_("Название фермы"))
    location = models.CharField(max_length=255, verbose_name=_("Местоположение"))
    
    def __str__(self):
        return self.farm_name

# 3 Теги товаров
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Тег"))

    def __str__(self):
        return self.name

# 4 Сам товар One-to-Many с Category и Farmer, Many-to-Many с Tag
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Название товара"))
    description = models.TextField(verbose_name=_("Описание"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена (KZT)"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name=_("Категория"))
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="products", verbose_name=_("Фермер"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Теги"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата добавления"))

    def __str__(self):
        return self.name

# 5 Заказ покупателя
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', _('В ожидании')),
        ('completed', _('Завершен')),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name=_("Покупатель"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата заказа"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name=_("Статус"))

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer.username}"

# 6 Элементы заказа
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.quantity} шт. - {self.product.name}"

# 7 Отзывы 
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", verbose_name="Товар")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв на {self.product.name}"