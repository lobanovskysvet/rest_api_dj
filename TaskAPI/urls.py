"""TaskAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework import routers
from TaskApp.views import RegistrationView
<<<<<<< HEAD
from django.conf.urls import url , include
=======
from django.conf.urls import url
>>>>>>> 9086234d442086cbb71b021b174feac5cb00a949
from TaskApp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/signup/$', RegistrationView.as_view(), name='registration_view'),
    url(r'^api/user/$', views.UserViewList.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)/$', views.UserViewDetail.as_view()),
<<<<<<< HEAD
   ]
=======
]
>>>>>>> 9086234d442086cbb71b021b174feac5cb00a949
