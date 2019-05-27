
from django.urls import path,include
from . import views
urlpatterns = [
    path('api/',views.ListUser),
    path('api/<int:id>/',views.DetailView),
]
