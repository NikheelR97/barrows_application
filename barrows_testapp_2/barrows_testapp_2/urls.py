from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView


from barrows_testapp_2.clients import views as client_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^clients/$', client_views.client_list, name='client_list'),
    url(r'^clients/create/$', client_views.client_create, name='client_create'),
    url(r'^clients/(?P<pk>\d+)/update/$', client_views.client_update, name='client_update'),
    url(r'^clients/(?P<pk>\d+)/delete/$', client_views.client_delete, name='client_delete'),
]
