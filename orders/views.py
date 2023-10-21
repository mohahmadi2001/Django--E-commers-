from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .forms import CartAddForm
from .cart import Cart
from home.models import Product
from orders.models import Order,OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin



class CartView(View):
    def get(self,request):
        cart = Cart(request)
        return render(request,"orders/cart.html",{'cart':cart})


class AddCartView(View):
    def post(self,request,product_id):
        cart = Cart(request)
        product = get_object_or_404(Product,id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product,form.cleaned_data['quantity'])
        return redirect("orders:cart")
    

class RemoveCartView(View):
    def get(self,request,product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)        
        cart.remove(product)
        return redirect('orders:cart')
    
class OrderDetailView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        order = get_object_or_404(Order,id=order_id)
        return render(request,'orders/order.html',{'order':order})
    

class OrderCreateView(LoginRequiredMixin,View):
    def get(self,request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )
            cart.clear()
        return redirect("orders:order_detail",order.id)