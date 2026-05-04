from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

# Форма реги
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email']

# Форма валидация
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'farmer', 'tags']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Бағасы 0-ден үлкен болуы керек!")
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError("Атауы тым қысқа!")
        return name