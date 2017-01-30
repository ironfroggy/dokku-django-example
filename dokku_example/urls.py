from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from count import views

urlpatterns = [
    url(r'^$', views.count, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
