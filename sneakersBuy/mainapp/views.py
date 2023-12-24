from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category, Brand

from basketapp.models import Basket


def get_data(**kwargs):
    links_menu = [
        {'link': 'index', 'name': 'Home'},
        {'link': 'products:index', 'name': 'Products'},
        {'link': 'about', 'name': 'About Us'},
        {'link': 'contacts', 'name': 'Contacts'},
    ]

    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'links_menu': links_menu,
        'categories': categories,
        'brands': brands,
    }

    context.update(**kwargs)
    return context


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def index(request):
    title = "Главная"
    basket = get_basket(request.user)
    prods = Product.objects.all()
    brands = Brand.objects.all()
    context = get_data(title=title, prods=prods, basket=basket, brands=brands)
    return render(request, 'index.html', context)


def about(request):
    title = "Информация"
    basket = get_basket(request.user)
    context = get_data(title=title, basket=basket)
    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"
    basket = get_basket(request.user)
    context = get_data(title=title, basket=basket)
    return render(request, 'contacts.html', context)


def products(request, category_pk=None, brand_id=None):
    prods = Product.objects.order_by('price')
    title = "Каталог продуктов"
    context = {}

    basket = get_basket(request.user)

    category = None
    brand = None

    if category_pk is not None:
        category = get_object_or_404(Category, pk=category_pk)
        prods = prods.filter(category=category)

    if brand_id is not None:
        brand = get_object_or_404(Brand, pk=brand_id)
        prods = prods.filter(brand=brand)

    context = get_data(title=title, prods=prods, basket=basket, category=category, brand=brand)
    return render(request, 'products.html', context)


def product(request, pk):
    title = "Продукт"
    prod = Product.objects.get(pk=pk)
    basket = get_basket(request.user)
    same_prods = Product.objects.exclude(pk=pk).filter(category=prod.category)
    context = get_data(title=title, prod=prod, same_prods=same_prods, basket=basket)
    return render(request, 'product.html', context)

