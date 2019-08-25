from django import template

register = template.Library()


@register.filter
def basket_total_quantity(basket):
    total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
    return total_quantity


@register.filter
def basket_total_cost(basket):
    total_cost = sum(list(map(lambda basket_slot: basket_slot.cost, basket)))
    return total_cost