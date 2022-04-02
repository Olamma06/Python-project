from django.urls import path

from . import views

urlpatterns=[
    path("", views.Home),
    path("about-us",views.aboutUs),
    path("mobile",views.contactUs)

]