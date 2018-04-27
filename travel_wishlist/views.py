from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, PlaceInfoForm #import form objects

# Create your views here.
def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save() #this creates a new place object from the form
        if form.is_valid(): #this validates database constraints
            place.save() #saves place to the database
            return redirect('place_list') #this redirects to a GET request
    '''if the request method is not POST, or the form is not valid, then display
    list of places and a form to add a new place.'''
    places = Place.objects.filter(visited=False).order_by('name')# sort places by name
    new_place_form = NewPlaceForm() # a form object added
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form' : new_place_form})
    # visited = Place.objects.filter(visited = True)
    # return render(request, 'travel_wishlist/visited.html', {'visited': visited})

'''request for the places that have been visited from the database and display them'''
def places_visited(request):
    visited = Place.objects.filter(visited = True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

# def place_is_visited(request):
#     if request.method == 'POST':
#         pk = request.POST.get('pk')#search primary key
#         place = get_object_or_404(Place, pk = pk) #search places by primary key
#         place.visited = True #set the boolean flag to True
#         place.save() # save the place in the database
#     return redirect('place_list')

def place_info(request, pk):
    #pk = request.POST.get(pk)
    place = get_object_or_404(Place, pk = pk)
    if not place.visited:
        form = PlaceInfoForm()
        if request.method == 'POST':
            form = PlaceInfoForm(request.POST)
            if form.is_valid():
                place = form.save()
                place.visited = True
                place.save()
        return render(request, 'travel_wishlist/info.html', {'place': place,'form': form})
    return render(request, 'travel_wishlist/info.html', {'place' : place})
