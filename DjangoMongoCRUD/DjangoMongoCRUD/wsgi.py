"""
WSGI config for DjangoMongoCRUD project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoMongoCRUD.settings')

application = get_wsgi_application()

from DjangoCRUDapp.urls import router as main_router


app = FastAPI(
    title="GIG",
    description="Creación de apis para GIG",
    version="Beta",
)

app.include_router(main_router, prefix="/api")