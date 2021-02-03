from django.urls import path

from basket.views import basket_add, basket_remove

app_name = 'basket'

urlpatterns = [
    path('basket-add/', basket_add, name='basket_add'),
    path('basket-remove/', basket_remove, name='basket_remove'),
]