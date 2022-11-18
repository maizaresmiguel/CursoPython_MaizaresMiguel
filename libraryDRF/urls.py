from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.book.api.routers')), #importamos la ruta definian en books
    # path('author/', include('apps.book.api.routers')), #importamos la ruta definian en books
]
