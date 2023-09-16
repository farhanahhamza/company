from django.urls import path
from .views import *

urlpatterns=[
    path('r',register,name="register"),
    path('su',success_page,name="success_page"),
    path('s',course_showcase,name="course_showcase"),
    path('so',soft,name="soft"),
    path('m',mearn,name="mearn"), 
    path('d',data,name="data"),
    path('p',python,name="python"),
    path('a',asp,name="asp"),
    path('an',android,name="android"),
    path('das',ds,name="ds"),
    path('j',java,name="java"),
]