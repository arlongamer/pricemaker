from django.urls import path
from . import views

urlpatterns = [
    path('', views.price_entry_view, name='price_entry'),
]
