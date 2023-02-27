from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Product


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","email","username","password1","password2"]
        
        
class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ["pname","Price","img"]