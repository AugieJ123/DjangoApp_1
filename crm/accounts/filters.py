import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Mete:
        model = Order
        fields = '__all__'