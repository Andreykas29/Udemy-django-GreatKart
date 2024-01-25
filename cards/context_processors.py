from cards.models import Cart, CartItem
from cards.views import _cart_id


def cart_quantity(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart[:1])
    quantity = 0
    for i in cart_items:
        quantity += i.quantity
    return {'cart_quantity': quantity}
