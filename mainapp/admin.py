from django.contrib import admin
from .models import Category, Farmer, Tag, Product, Order, OrderItem, Review

# рега моделей
admin.site.register(Category)
admin.site.register(Farmer)
admin.site.register(Tag)
admin.site.register(OrderItem)
admin.site.register(Review)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Displaying the table with attributes (какие колонки показывать в списке)
    list_display = ('name', 'price', 'category', 'farmer', 'created_at')
    
    # Adding list filters (панель фильтрации справа)
    list_filter = ('category', 'farmer', 'created_at')
    
    # Adding search functionality (строка поиска по названию и описанию)
    search_fields = ('name', 'description')
    
    # Adding sorting attribute (сортировка по умолчанию - по дате добавления по убыванию)
    ordering = ('-created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username',)
    ordering = ('-created_at',)