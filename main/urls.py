from django.urls import path
from .views import *

urlpatterns = [
    path('get-user/', get_user),
    path('get-token/', get_token),
    path('get-clients/', get_clients),
    path('get-product/', get_product),
    path('get-order/', get_order),
    path('create-client/', create_client),
    path('create-user/', create_user),
    path('create-order/', create_order),
    path('get-kassa/', get_kassa),
]