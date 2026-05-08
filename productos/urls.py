from django.urls import path
from . import views
# 2 punto de entrada y acá se manejan todas las rutas (url) de esta app
urlpatterns = [
path('', views.index, name='home_productos'),
]