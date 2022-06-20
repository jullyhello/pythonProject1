from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Order


class OrderList(ListView):
    model = Order
    ordering = '-pk'
   # template_name = 'order/order_list.html'


class OrderDetail(DetailView):
    model = Order

#def index(request):
 #   orders = Order.objects.all().order_by('-pk')
  #  return render(
   #     request,
    #    'order/order_list.html',
     #   {
      #      'orders': orders,
       # }
    #)

#def single_order_page(request, pk):
 #   orders = Order.objects.get(pk=pk)
  #  return render(
   #     request,
     #   'order/order_detail.html',
    #    {
      #      'orders' : orders,
       # }
    #)