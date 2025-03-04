from django import forms
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['total_amount']
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'form-control'})
            for field in Order._meta.get_fields()
            if field.get_internal_type() in ['CharField', 'TextField']
        }
        widgets['order_date'] = forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'})


OrderItemFormSet = forms.inlineformset_factory(
    Order,
    OrderItem,
    fields=['product', 'quantity'],
    extra=1,
    can_delete=False,
    widgets={
        'product': forms.Select(attrs={'class': 'form-control'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control'})
    }
)
