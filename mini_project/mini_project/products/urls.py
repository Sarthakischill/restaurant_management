from django.urls import path
from . import views


urlpatterns = [
    path('NonVeg', views.nonveg),
    path('Veg', views.veg),
    path('Bev', views.bev),
    path('order', views.order),
    path('about', views.about)
]
