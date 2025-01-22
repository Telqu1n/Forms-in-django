from django.urls import path
from .import views

urlpatterns = [
    path('', views.LogInFormView.as_view(), name='index'),
    path ('test', views.ThankYouView.as_view(), name='test'),
    path('users', views.UserInfoView.as_view(), name='users'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user_info'),
    
]

