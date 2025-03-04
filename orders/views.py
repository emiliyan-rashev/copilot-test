from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import OrderForm, OrderItemFormSet
from django.views.generic import ListView
from .models import Order, OrderItem


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = OrderItemFormSet(self.request.POST, prefix='items')
        else:
            data['items'] = OrderItemFormSet(prefix='items')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        self.object = form.save()
        if form.is_valid() and items.is_valid():
            order_items = []
            total_amount = 0
            for form in items.forms:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    quantity = form.cleaned_data.get('quantity')
                    if quantity and quantity > 0:
                        item = form.save(commit=False)
                        item.order = self.object
                        order_items.append(item)
                        total_amount += item.product.price * quantity
            if order_items:
                OrderItem.objects.bulk_create(order_items)
            self.object.total_amount = total_amount
            self.object.save()
            return redirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form, items=items))


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
