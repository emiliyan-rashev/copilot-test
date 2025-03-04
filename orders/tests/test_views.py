from django.test import TestCase, Client
from django.urls import reverse
from orders.models import Order, OrderItem
from products.models import Product
from django.utils import timezone
import json


class CreateOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product1 = Product.objects.create(
            name='Product 1',
            price=10.00,
            description='Description for product 1'
        )
        self.product2 = Product.objects.create(
            name='Product 2',
            price=20.00,
            description='Description for product 2'
        )
        self.create_order_url = reverse('create_order')

    def test_create_order(self):
        order_data = {
            'customer_name': 'Jane Doe',
            'customer_email': 'jane@example.com',
            'order_date': timezone.now().isoformat(),
            'items': [
                {'product_id': self.product1.id, 'quantity': 1},
                {'product_id': self.product2.id, 'quantity': 2}
            ]
        }
        response = self.client.post(
            self.create_order_url,
            data=json.dumps(order_data),
            content_type='application/json'
        )
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 2)

        order = Order.objects.first()
        self.assertEqual(order.customer_name, 'Jane Doe')
        self.assertEqual(order.customer_email, 'jane@example.com')
        self.assertEqual(order.total_amount, 50.00)

        order_item1 = OrderItem.objects.get(product=self.product1)
        self.assertEqual(order_item1.quantity, 1)
        self.assertEqual(order_item1.product.price, 10.00)

        order_item2 = OrderItem.objects.get(product=self.product2)
        self.assertEqual(order_item2.quantity, 2)
        self.assertEqual(order_item2.product.price, 20.00)
