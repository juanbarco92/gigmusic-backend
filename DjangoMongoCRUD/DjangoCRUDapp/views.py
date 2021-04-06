from django.shortcuts import render
from DjangoCRUDapp.models import Artista
# Create your views here.

 
def searchbar(request):
    if request.method == 'POST':
        search = request.POST['search']
        query = Artista.objects.filter(artista__contains=search)

        return render(request, 
            'searchbar.html', 
            {'search':search,
            'artista':query})
    else:
        return render(request, 
        'searchbar.html', 
        {}) 
