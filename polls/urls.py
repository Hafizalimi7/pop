
from django.urls import path
from polls import views

urlpatterns = [
    
    path('Our_home/', views.home)
]
