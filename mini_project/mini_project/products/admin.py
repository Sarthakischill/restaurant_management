from django.contrib import admin
from .models import Vegetarian
from .models import NonVegetarian
from .models import Beverages


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')


admin.site.register(Vegetarian, ProductAdmin)
admin.site.register(NonVegetarian, ProductAdmin)
admin.site.register(Beverages, ProductAdmin)
