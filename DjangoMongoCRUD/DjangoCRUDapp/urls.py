from fastapi import APIRouter

from DjangoCRUDapp import views
from DjangoCRUDapp.models import ArtistaAPI

router = APIRouter()

router.get(
    "/search/{artista}",
    summary="Devuelve un artista con su discografia",
    response_model=ArtistaAPI,
    name="artist-get",
)(views.artist_get)