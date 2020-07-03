from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:pk>/', views.place_details, name='place_details'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

