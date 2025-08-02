from django.urls import path
from . import views

urlpatterns = [
    path('execute_submission/', views.execute_submission),
]
