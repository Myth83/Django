from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/main.html')


def products(request, pk=None):
    product_list = Product.objects.all()
    if pk:
        product_list = product_list.filter(category__pk=pk)

    if request.user.is_authenticated:
        context = {'products': product_list,
                   'categories': ProductCategory.objects.all(),
                   'basket': request.user.basket.all()
                   }
    else:
        context = {'products': product_list,
                   'categories': ProductCategory.objects.all(),
                   }

    return render(request, 'mainapp/products.html', context=context)


def contacts(request):
    context = {'contacts': ['yandex@yandex.ru', 'shmandex@shmandex.ru']}
    return render(request, 'mainapp/contacts.html', context=context)
