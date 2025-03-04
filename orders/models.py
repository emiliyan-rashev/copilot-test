from django.db import models


class Order(models.Model):
    order_date = models.DateTimeField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    shipping_address = models.TextField()
    billing_address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
