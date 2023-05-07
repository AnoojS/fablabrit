from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import gallery

urlpatterns = [
    path('', gallery, name='gallery')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)