# """
# TeyvatMap URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """


from django.conf.urls import url

from . import views

urlpatterns = [
    ## FRONTEND DIST
    url(r'^$', views.index),
    url('index/', views.index),
    ## PRODUCTION_UNITE_SELECT
    url('api/getMapInfo', views.get_data),
    ## PRODUCTION_SINGLE_SELECT
    url('get/note/', views.get_note),
    url('put/note/', views.put_note),
    url('get/build_data/', views.get_build_data),
]
