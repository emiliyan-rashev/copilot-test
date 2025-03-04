from django.test import TestCase
from products.models import Product


class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=15.00,
            description='Test Description'
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 15.00)
        self.assertEqual(self.product.description, 'Test Description')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_price(self):
        self.assertTrue(self.product.price > 0)
