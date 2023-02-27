from django.shortcuts import render
from Home.models import Product


def ItemSingleView(request,pk):
    product = Product.objects.filter(pid = pk)
    context = {
        "product":product
    }
    return render(request,'itemsingleview.html',context)
