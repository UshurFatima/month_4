from django.shortcuts import render
from . import models


def eat_list_view(request):
    if request.method == 'GET':
        product_eat = models.Product.objects.filter(tags__name='еда').order_by('-id')
        product_electronic = models.Product.objects.filter(tags__name='электроника').order_by('-id')
        return render(
            request,
            template_name='filter_list.html',
            context={
                'product_eat': product_eat,
                'product_electronic': product_electronic
            },
        )
