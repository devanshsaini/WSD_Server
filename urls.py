from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simple_lesk.urls')),
    path('', include('resnik.urls')),
    path('', include('simple_lesk.urls')),
]
