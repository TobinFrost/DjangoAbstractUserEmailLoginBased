"""othercustom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.contrib.auth import forms as auth_form
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from simple.models import MyUser
from simple.forms import MyUserCreationForm
from simple import views as simpleviews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(
        template_name= 'home.html'
    )),
    url(r'^login/',auth_view.login,{
        'template_name': 'login.html'},name= "login"),
    url(r'^register/',CreateView.as_view(
        template_name= "register.html",
        form_class= MyUserCreationForm,
        success_url= "/",
    ),name="register"),
    url(r'^register_etudiant/',simpleviews.register,name="register_etudiant"),
    #url('^accounts/', include('django.contrib.auth.urls')),
    url('^accounts/profile', simpleviews.home),
    url(r'^logout/$',simpleviews.logout,name="logout"),
]
