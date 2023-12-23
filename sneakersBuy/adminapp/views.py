from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import Category, Product


def user_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': user_list,
    }

    return render(request, 'adminapp/users.html', context)


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


def category_create(request, pk):
    pass


def categories(request):
    title = 'админка/категории'
    category_list = Category.objects.all()

    context = {
        'title': title,
        'objects': category_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def product_create(request, pk):
    pass


def products(request, pk):
    title = 'админка/продукты.'
    category = get_object_or_404(Category, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': product_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_read(request, pk):
    pass


