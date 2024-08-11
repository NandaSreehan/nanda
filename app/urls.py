from django.urls import path
from app import views
urlpatterns=[
    path('details',views.details,name="dtls"),
    path("single/<str:s>",views.single,name="sala"),
    path("prime/<int:s>",views.prime,name="sa"),
    path("perfect/<int:s>",views.perfect,name="sal")



]