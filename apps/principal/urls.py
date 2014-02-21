from django.conf.urls import patterns, include, url
from .views import CrearCBV,ListarCBV,DetalleCBV


urlpatterns = patterns('',
   url(r'^$', 'apps.principal.views.CrearFBV'),
   url(r'^listar-FBV/$', 'apps.principal.views.ListarFBV'),

   url(r'^crear-CBV/$' , CrearCBV.as_view()),
   url(r'^listar-CBV/$' , ListarCBV.as_view()),
   url(r'^detalle-CBV/(?P<pk>\d+)/$' , DetalleCBV.as_view()),
)
