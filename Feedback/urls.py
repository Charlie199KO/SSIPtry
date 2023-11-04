"""
URL configuration for Feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Form import views

'''
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form, name='form'),
    path('portal/', views.portal, name='portal'),
    path('feedback/', views.feedback, name='feedback'),
    path('trial/', views.trial, name='trial'),
    path('compliment/', views.compliment, name='compliment'),
    path('suggestion/', views.suggestion, name='suggestion'),
    path('incident/', views.incident, name='incident'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('login/', views.signin, name='login'),
]
'''
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
'''

'''    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path.*)$',serve,{'document_root': settings.STATIC_ROOT}),'''
