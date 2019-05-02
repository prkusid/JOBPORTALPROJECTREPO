"""JOBPORTALPROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from jobapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome),
    url(r'^register/', views.register),
    url(r'^index/', views.index),
    url(r'^apply/(?P<slug>[-\w]+)/(?P<designation>[-\w]+)/(?P<city>[-\w]+)/$', views.apply,),
    url(r'^thanks/', views.thanks),
    url(r'^about_us1/', views.aboutus1),
    url(r'^about_us2/', views.aboutus2),
    url(r'^applied/', views.applied),
    url(r'^details/(?P<slug>[-\w]+)/(?P<designation>[-\w]+)/(?P<city>[-\w]+)/$', views.details),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
