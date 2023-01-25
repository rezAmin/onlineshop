from django.urls import path, include

from . views import ProductListView

urlpatterns = [
     path('', ProductListView.as_view(), name='products_list'),

]