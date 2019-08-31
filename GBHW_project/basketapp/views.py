from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import BasketSlot
from mainapp.models import Product


def add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.user.is_authenticated:
        basket_slot = request.user.basket.filter(product=product).first()
        if basket_slot:
            basket_slot.quantity += 1
            basket_slot.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            basket_slot = BasketSlot(user=request.user, product=product)
            basket_slot.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(reverse_lazy('authapp:login'))


def remove(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.user.is_authenticated:
        basket_slot = request.user.basket.filter(product=product).first()
        if basket_slot:
            if basket_slot.quantity > 1:
                basket_slot.quantity -= 1
                basket_slot.save()
            else:
                basket_slot.delete()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            basket_slot = BasketSlot(user=request.user, product=product)
            basket_slot.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(reverse_lazy('authapp:login'))
