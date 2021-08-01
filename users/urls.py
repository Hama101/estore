
from django.urls import path 
from . import views as v

f="#"
urlpatterns = [
    path('log-in/',v.log_in , name="log-in"),
    path('sign-up/',v.sign_up,name="sign-up"),
    path('logout/', v.logoutUser, name="logout"),
    
    path(f'my-profile/<str:username>/',v.my_profile , name="my-profile"),
    path('make-profile/',v.make_profile , name="make-profile"),
]

