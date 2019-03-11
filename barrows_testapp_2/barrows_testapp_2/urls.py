from django.conf.urls import url
from django.contrib import admin


from clients import views as client_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),


]
