from django.urls import path
from .views import *


app_name ='products'


urlpatterns = [
    path('', products_home, name='products_page'),
]

