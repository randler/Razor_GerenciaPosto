from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from CONAB.gasto.models import Combustivel,Servico
from django.views.generic import ArchiveIndexView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'CONAB.gasto.views.home', name='home'),
    # url(r'^CONAB/', include('CONAB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gasto', ArchiveIndexView.as_view(model=Combustivel, date_field='data_abastecido'))
)
