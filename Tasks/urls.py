from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('update/<str:pk>/', views.update_task, name="update"),

]