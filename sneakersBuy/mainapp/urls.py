from django.urls import path
from mainapp.views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('product/<int:pk>/', product, name='product'),
    path('category/<int:category_pk>/', products, name='category'),
    path('brand/<int:brand_id>/', products, name='brand'),
    path('category/<int:category_pk>/brand/<int:brand_id>/', products, name='category_with_brand'),
]
