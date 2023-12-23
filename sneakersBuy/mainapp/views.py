from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category

from basketapp.models import Basket


def get_data(**kwargs):
    links_menu = [
        {'link': 'index', 'name': 'Home'},
        {'link': 'products:index', 'name': 'Products'},
        {'link': 'about', 'name': 'About Us'},
        {'link': 'contacts', 'name': 'Contacts'},
    ]

    categories = Category.objects.all()

    context = {
        'links_menu': links_menu,
        'categories': categories,
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
    context = get_data(title=title, prods=prods, basket=basket)
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


def products(request, pk=None):
    prods = Product.objects.order_by('price')
    title = "Каталог продуктов"
    context = {}

    basket = get_basket(request.user)

    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        prods = Product.objects.filter(category__pk=pk).order_by('price')
        context = get_data(category=category)

    context = get_data(title=title, prods=prods, basket=basket, **context)
    return render(request, 'products.html', context)


def product(request, pk):
    title = "Продукт"
    prod = Product.objects.get(pk=pk)
    basket = get_basket(request.user)
    same_prods = Product.objects.exclude(pk=pk)
    context = get_data(title=title, prod=prod, same_prods=same_prods, basket=basket)
    return render(request, 'product.html', context)
