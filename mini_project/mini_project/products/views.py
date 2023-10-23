from django.http import HttpResponse
from django.shortcuts import render
from .models import Vegetarian
from .models import NonVegetarian
from .models import Beverages


def veg(request):
    veg = Vegetarian.objects.all
    return render(request, 'index.html', {'veg': veg})


def nonveg(request):
    nonveg = NonVegetarian.objects.all
    return render(request, 'index.html', {'nonveg': nonveg})


def bev(request):
    bev = Beverages.objects.all
    return render(request, 'index.html', {'bev': bev})


def order(request):
    return render(request, 'order.html')


def about(request):
    return render(request,'about.html')

