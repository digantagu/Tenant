from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Hello Admin"
admin.site.site_title = "TM's Admin Portal"
admin.site.index_title = "Welcome to TM's Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
