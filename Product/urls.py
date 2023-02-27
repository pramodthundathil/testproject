from django.urls import path 
from .import views

urlpatterns = [
    path("ItemSingleView/<int:pk>",views.ItemSingleView,name="ItemSingleView")
]
