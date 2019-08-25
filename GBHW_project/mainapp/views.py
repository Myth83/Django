from django.shortcuts import render
from .models import Product


def main(request):
    return render(request, 'mainapp/main.html')


def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context=context)


def contacts(request):
    context = {'contacts': ['yandex@yandex.ru', 'shmandex@shmandex.ru']}
    return render(request, 'mainapp/contacts.html', context=context)
