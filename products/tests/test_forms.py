from django.test import TestCase
from products.forms import ProductForm


class ProductFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'Test Product',
            'price': 10.99,
            'description': 'A test product description',
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'price': 'invalid_price',
            'description': 'A test product description',
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
