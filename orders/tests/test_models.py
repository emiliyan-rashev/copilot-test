from django.test import TestCase
from orders.models import Order, OrderItem
from products.models import Product
from django.utils import timezone


class OrderModelTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            customer_name='John Doe',
            customer_email='john@example.com',
            order_date=timezone.now(),
            total_amount=0
        )
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='A test product'
        )

    def test_order_creation(self):
        self.assertEqual(self.order.customer_name, 'John Doe')
        self.assertEqual(self.order.customer_email, 'john@example.com')
        self.assertEqual(self.order.total_amount, 0)

    def test_order_item_creation(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.product.price, 10.00)
