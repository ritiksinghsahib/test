from django.urls import path
from .import views
urlpatterns =[
    path("",views.index ,name="Home"),
    path("services/",views.ser,name="services"),
    path("event/",views.event,name="Event"),
] 