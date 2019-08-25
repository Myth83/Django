from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/main.html')


def products(request, pk=None):
    product = Product.objects.all()
    if request.user.is_authenticated:
        if pk or pk == 0:
            if pk != 0:
                category = get_object_or_404(ProductCategory, pk=pk)
                product = product.filter(category=category)
            context = {'products': product, 'categories': ProductCategory.objects.all(), 'basket': request.user.basket.all()}
            return render(request, 'mainapp/products.html', context)
        else:
            hot_product = Product.objects.filter(is_hot=True).first()
            context = {'hot_product': hot_product, 'categories': ProductCategory.objects.all(), 'basket': request.user.basket.all()}
            return render(request, 'mainapp/hot_product.html', context)
    else:
        context = {'products': product, 'categories': ProductCategory.objects.all(),}
        return render(request, 'mainapp/products.html', context=context)



    # product_list = Product.objects.all()
    # if pk:
    #     product_list = product_list.filter(category__pk=pk)
    #
    # if request.user.is_authenticated:
    #     context = {'products': product_list,
    #                'categories': ProductCategory.objects.all(),
    #                'basket': request.user.basket.all()
    #                }
    # else:
    #     context = {'products': product_list,
    #                'categories': ProductCategory.objects.all(),
    #                }
    #
    # return render(request, 'mainapp/products.html', context=context)


def contacts(request):
    context = {'contacts': ['yandex@yandex.ru', 'shmandex@shmandex.ru']}
    return render(request, 'mainapp/contacts.html', context=context)
