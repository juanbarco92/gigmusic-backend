from django.shortcuts import render
from DjangoCRUDapp.models import Artista
# Create your views here.

 
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        search = Artista.objects.all().filter(artista=query)

        return render(request, 'searchbar .html', {'post':search})