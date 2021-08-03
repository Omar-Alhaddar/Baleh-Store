from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('reglog.urls')),
    path('', include('whole.urls')),
    path('admin/', admin.site.urls)
]
