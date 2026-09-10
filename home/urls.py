from django.urls import path
from home.views import home, iniciar_sesion, registro, listado_de_pinturas, ver_pintura, crear_pintura, EditarPintura, EliminarPintura  #
from django.contrib.auth.views import LogoutView  #

urlpatterns = [
    path('', home, name='home'),
    path('pinturas/', listado_de_pinturas, name='listar_pinturas'),
    path('ver_pintura/<int:pk>', ver_pintura, name='ver_pintura'),
    path('crear_pintura/', crear_pintura, name='crear_pintura'),
    path('editar_pintura/<int:pk>', EditarPintura.as_view(), name='editar_pintura'),  #
    path('eliminar_pintura/<int:pk>', EliminarPintura.as_view(), name='eliminar_pintura'),   #
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),  #
    path('cerrar_sesion/', LogoutView.as_view(template_name='home/cerrar_sesion.html'), name='cerrar_sesion'),  #
    path('registro/', registro, name='registro'),  #
]