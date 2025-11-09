from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('panel-vigilante/', views.panel_vigilante, name='panel_vigilante'),
    path('panel-usuario/', views.panel_usuario, name='panel_usuario'),
]
