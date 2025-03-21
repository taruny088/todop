from django.urls import path
from .views import *

urlpatterns = [
    path('',reg),
    path('data/',details,name='details'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('specific_detail/<int:id>/',specific_detail,name='specific_detail'),
]