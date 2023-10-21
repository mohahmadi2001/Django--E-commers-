from django.db import models
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="orders")
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('paid','-update')
        
    def __str__(self):
        return f'{self.user} - {str(self.id)}'
    
    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey('home.Product',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity