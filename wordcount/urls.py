

from django.urls import path
from . import views

# ##Este espacio define los nombres de las páginas disponibles
urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
]
