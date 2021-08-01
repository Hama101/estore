
from django.urls import path 
from . import views as v


urlpatterns = [
    path('',v.home,name="home"),
    path('category/<str:title>/',v.category,name="category"),
    path('product/<str:pk>/',v.view_product, name="product"),
]

