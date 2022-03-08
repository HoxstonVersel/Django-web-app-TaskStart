from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path, include


from freelance.views import *


from django.views.generic.base import RedirectView


from taskstart import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('freelance.urls')),  # http//:ip:port/freelance (Главная страница)
    path('chat/', include('chat.urls')), # http//:ip:port/chat
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound