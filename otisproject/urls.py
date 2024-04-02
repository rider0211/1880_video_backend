"""
URL configuration for otisproject project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/auth/', include('user.urls')),
    path('api/v1/admin/', include('management.urls')),
    path('api/v1/customer/', include('customer.urls')),
    path('api/v1/coloringpages/', include('coloringpage.urls')),
    path('api/v1/email/', include('emailmanagement.urls'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)