from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('details.urls')),
    path('department/', include('department.urls')),
]