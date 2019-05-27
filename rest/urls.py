
from django.urls import path,include
from . import views
urlpatterns = [
    path('api/',views.ListUser.as_view()),
    path('api/<int:id>/',views.DetailView.as_view()),
]
