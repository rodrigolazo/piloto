from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'aplicacion1.views.mostrarTexto'),

    url(r'tabla/', 'aplicacion1.views.mostrarTabla'),
    url(r'insertar/', 'aplicacion1.views.formulario'),
     url(r'borrar/(?P<id_persona>\d+)$','aplicacion1.views.eliminar_persona'),
      url(r'editar/(?P<id_persona>\d+)$','aplicacion1.views.editar_persona'),
    # r'^$' nos indica que estamos haciendo referencia al index de nuestro proyecto
    # aplicacion1 es el nombre de nuestra aplicacion, views el archivo que contiene todas las vistas y mostrarTexto es el nombre de la vista que queremos mostrar
)
