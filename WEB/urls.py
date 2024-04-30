"""
URL configuration for WEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include
from . import views
from .views import edit_profile
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('<int:pk>/', views.get_video, name='video'),
    path('guided-meditation/', views.get_list_video, name='guided-meditation'),
    path('faq/', views.faq, name='faq'),
    path('', views.home, name="home"),
    path('', include("allauth.urls")),
    path('', include('feedback.urls')),
    path('forum/', include('Forum.urls')),
    path('', include('Progress.urls')),
    path('', include('Challenge.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
