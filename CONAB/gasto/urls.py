from django.conf.urls import patterns, include, url
#from .views import index,index2

urlpatterns = patterns('',

     url(r'^$', 'django.contrib.auth.views.login',
         {'template_name': 'inicio/index.html'}, name='login'),

    url(r'^fechar/$', 'django.contrib.auth.views.logout_then_login',
          name='logout'),


)
