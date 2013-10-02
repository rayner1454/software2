from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# Es importante declarar esta linea para la subida de imagenes 
# ademas puedan ser visualizadas 
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ubicatech.views.home', name='home'),
    # url(r'^ubicatech/', include('ubicatech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #Agregamos el modulo de Grappelli en el proyecto
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Es importante esta linea de codigo porque sin esta linea de codigo no se podran visualizar las imagenes
    # ademas que tiene la opcion para que se direccion correctamente hasta la ubicacion de la imagen
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    # La siguiente linea de codigo sirve para incluir las opciones del Editor de Texto con opciones parecdidas a Word
    (r'^ckeditor/', include('ckeditor.urls')),
)
