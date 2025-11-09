from django.urls import path
from web.views import registro_usuario, login_view

urlpatterns = [
    path('', registro_usuario, name='home'),
    path('login/', login_view, name='login'),
]