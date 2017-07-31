from django.conf.urls import url
from django.contrib import admin
from buscar import views

urlpatterns = [
	
	url(r'^$', views.index),
	url(r'^resultado/(?P<texto>[\w-]+)', views.resultado, name="resultado"),
	url(r'^body/(?P<protocolo>[\w-]+)', views.body, name="body"),
    url(r'^admin/', admin.site.urls),
]


