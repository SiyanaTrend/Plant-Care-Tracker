from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterAppUserView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', views.AppUserLogoutView.as_view(), name='logout'),
]