from django.urls import path
from .import views

urlpatterns = [
    path('', views.LogInFormView.as_view(), name='index'),
    path ('test', views.about, name='test'),
]

