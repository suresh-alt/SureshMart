"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views
from product import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name='main'),
    path('home/',views.home,name='home'),
    path('save/',views.save,name='save'),
    path('admin1/',views.admin,name='admin1'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('addp/',views.addp,name='addp'),
    path('savep/',views.savep,name='savep'),
    path('viewall/',views.viewall,name='viewall'),
    path('updatepro/',views.updatepro,name='updatepro'),
    path('ud/',views.ud,name='ud'),
    path('del/',views.delete,name='delete'),
    path('clogin/',views.clogin,name='clogin'),
    path('c/',views.c,name='c'),
    path('h1/',views.h1,name='h1'),
    path('vpro/',views.vpro,name='vpro'),
    path('cart/',views.cart,name='cart'),
    path('cartview/',views.cartview,name='cartview'),
    path('cartdelete/',views.cartdelete,name='cartdelete'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

