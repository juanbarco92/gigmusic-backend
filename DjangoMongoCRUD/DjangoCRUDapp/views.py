from fastapi import Body, Depends

from .models import ArtistaAPI
from .models import ArtistaAPIS
from .models import Artista
from .utils import get_artist


from django.shortcuts import render
from DjangoCRUDapp.models import Artista
# Create your views here.


def artist_get(
    artist: Artista = Depends(get_artist),
) -> ArtistaAPI:

    """
    Devuelve un objeto artista especifico
    """
    return ArtistaAPI.from_model(artist)
 
"""
def searchbar(request):
    if request.method == 'POST':
        search = request.POST['search']
        query = Artista.objects.all().filter(artista__contains=search)
        if query:
            q = query[0].artista
            q = query[0].canciones
        else: 
            q=query

        return render(request, 
            'searchbar.html', 
            {'search':search,
            'artista':q})
    else:
        return render(request, 
        'searchbar.html', 
        {}) 
"""