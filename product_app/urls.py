
from django.contrib import admin
from django.urls import path, include

from product_app import views

urlpatterns = [
    path("", views.index , name="index"),
    path('index/addproduct' ,views.add_product, name="add_product"),
    path('index/deleteproduct/<int:product_id>',views.delete_product , name="delete_product"),
    path('index/updateproduct/<int:product_id>',views.update_product_details , name="update_product_details"),
]
