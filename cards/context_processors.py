from cards.models import Cart, CartItem
from cards.views import _cart_id


def cart_quantity(request):
    cart = Cart.objects.filter(cart_id=_cart_id(request))
    quantity = 0
    cart_items = CartItem.objects.all().filter(cart=cart[:1])
    for i in cart_items:
        quantity += i.quantity
    return {'cart_quantity': quantity}
