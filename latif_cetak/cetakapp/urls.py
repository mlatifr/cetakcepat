from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("delete/<str:product_id>/", views.delete_product, name="delete_product"),
]
