from django.urls import path
from . import views
# 2 punto de entrada y acá se manejan todas las rutas (url) de esta app
urlpatterns = [
    path('', views.index, name='home_productos'),
    path('login/', views.login, name='pepito'),
    path('register/', views.register, name='pepito'),
    path('dashboard/', views.dashboard, name='pepito'),
    path('venta/', views.venta, name='pepito'),
]