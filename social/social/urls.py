from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('caixa.urls')),
    path('dbv/', include('dbv.urls')),

]
