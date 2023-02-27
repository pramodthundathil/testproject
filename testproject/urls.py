from django.contrib import admin
from django.urls import path,include
from Home import views
from django.conf import settings
from django.conf.urls.static import static


from Product import urls
import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/",include("Product.urls")),
    path("",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("Index",views.Index,name="Index"),
    path("AddProduct",views.AddProduct,name="AddProduct"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
