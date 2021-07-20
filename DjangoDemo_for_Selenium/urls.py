"""DjangoDemo_for_Selenium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
import login.views as login_view
import register.views as register_view
import home.views as home_view

urlpatterns = [
    path('', login_view.load_login, name="login"),
    path('register/', register_view.register, name="register"),
    path('home/', home_view.load_home, name="home"),
    path('logout/', home_view.user_logout, name="logout"),
    path('history/', home_view.history, name="history"),
]
