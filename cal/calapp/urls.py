from django.urls import path
from . import views

urlpatterns=[
    path(r'',views.home,name='home'),
    path('add',views.add,name='add'),
    path('class1/',views.class1,name='class1'),


]
