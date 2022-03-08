"""
ASGI config for taskstart project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import chat.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskstart.settings')

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})

