from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='I am ignored, "Secret/" will do nothing')] ##This one is ignored because the one below overwrites it *I think atleast*
urlpatterns = [path('cum', views.index, name='This is the cum one')]  ##I presume name is solely for the in-web debugging and figuring out which is which