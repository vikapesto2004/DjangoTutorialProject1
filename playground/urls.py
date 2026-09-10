# Файл, в котором URL связываются с view-functions
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello)
]
# Было path('playground/hello/', views.say_hello), 
# но добавили в основные urls 