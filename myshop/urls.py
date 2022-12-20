"""myshop re_path Configuration

The `re_pathpatterns` list routes re_paths to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/re_paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to re_pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to re_pathpatterns:  path('', Home.as_view(), name='home')
Including another re_pathconf
    1. Import the include() function: from django.re_paths import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)