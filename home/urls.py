from django.urls import path
from home.views import home, listado_de_pinturas

urlpatterns = [
    path('', home),
    path('pinturas/', listado_de_pinturas)
]