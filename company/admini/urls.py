from django.urls import path
from .views import *

urlpatterns=[
    path('h',home,name="home"),
    path('ma',main,name="main"),
    path('sin',signin,name="signin"),
    path('sup',signup,name="signup"),
    path('c',course,name="course"),
]
