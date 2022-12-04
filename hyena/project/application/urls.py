from django.urls import path
from .views import HomePage, Signup, Signin,  logoutuser

urlpatterns = [
    
    path('home/', HomePage, name="home-page"),
    path('signup/', Signup, name="signup-page"),
    path('signin/', Signin, name="signin-page"),
    path('logout/', logoutuser, name="logout")
]