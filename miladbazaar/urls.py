
from django.contrib import admin
from django.urls import path
from market_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',home),
    path('shop/',shop),
    path('shop/<code>',show),
    path('blog/',blog),
    path('contact/',contact),
    path('services/',services),
    path('about/',about),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)