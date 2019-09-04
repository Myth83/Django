from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot

admin.site.register(ShopUser)


class BasketSlotInLine(admin.TabularInline):
    model = BasketSlot
    fields = 'product', 'quantity',
    extra = 0

class ShopUserWithBasket(ShopUser):
    class Meta:
        verbose_name = "Customer with basket"
        verbose_name_plural = "Customers with basket"
        proxy = True


@admin.register(ShopUserWithBasket)
class ShopUserWithBasketAdmin(admin.ModelAdmin):
    list_display = 'username', 'get_basket_quantity', 'get_basket_cost',
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketSlotInLine,

    def get_queryset(self, request):
        qs = super(ShopUserWithBasketAdmin, self).get_queryset(request)
        qs = qs.filter(basket__quantity__gt=0).distinct()
        return qs

    def get_basket_quantity(self, instance):
        basket = instance.basket.all()
        total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
        return total_quantity

    def get_basket_cost(self, instance):
        basket = instance.basket.all()
        total_cost = sum(list(map(lambda basket_slot: basket_slot.cost, basket)))
        return total_cost

    get_basket_quantity.short_description = 'Products in basket'
    get_basket_cost.short_description = 'Cost of basket'