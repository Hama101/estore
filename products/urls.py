
from django.urls import path 
from . import views as v


urlpatterns = [
    path('',v.home,name="home"),
    path('category/<str:title>/',v.category,name="category"),
    path('product/<str:pk>/',v.view_product, name="product"),
    
    path("save-to-wishlist/<str:pk>/" , v.save_to_wishlist , name="save-to-wishlist"),
    path("remove-from-wishlist/<str:pk>/" , v.remove_from_wishlist , name="remove-from-wishlist"),
]

