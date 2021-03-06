"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from  django.urls import path
from core import views
from django.views.generic import RedirectView #segunda forma de redirecionar pag inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_compromissos),
    path('agenda/lista', views.json_lista_compromisso),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/',views.logout_user),
    path('agenda/compromisso/', views.compromisso),
    path('agenda/compromisso/submit', views.submit_compromisso),
    path('agenda/compromisso/delete/<int:id_compromisso>/', views.delete_compromisso)


]
