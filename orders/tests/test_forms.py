from django.test import TestCase

from orders.forms import OrderForm


class TestOrderForm(TestCase):
    def test_order_form_valid_data(self):
        form_data = {
            'order_date': '2023-10-01T10:00',
            'product_id': 1,
            'quantity': 5,
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'shipping_address': '123 Main St',
            'billing_address': '123 Main St',
            'postal_code': '12345',
            'city': 'Anytown',
            'country': 'USA',
            'state': 'CA',
            'payment_method': 'Credit Card'
        }
        form = OrderForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_order_form_invalid_data(self):
        form_data = {
            'product_id': '',
            'quantity': '',
            'customer_name': '',
            'address': ''
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_order_form_missing_fields(self):
        form_data = {
            'product_id': 1,
            'quantity': 5
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
