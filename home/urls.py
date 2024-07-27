from django.urls import path
from .views import AuthView, LogoutView, RegisterView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
