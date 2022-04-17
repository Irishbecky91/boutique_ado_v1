"""
bag tools
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    calculates sub-total
    """
    return price * quantity
