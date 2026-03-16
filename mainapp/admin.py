from django.contrib import admin
from .models import Category, Farmer, Tag, Product, Order, OrderItem, Review

#7 модел рега жасау, админ панельде көріну үшін
admin.site.register(Category)
admin.site.register(Farmer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)