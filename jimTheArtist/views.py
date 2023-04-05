from django.shortcuts import render, get_object_or_404
import random
from .models import Painting

def home(request):
    return render(request, 'home.html')

def gallery(request):
    # Retrieve all paintings from the database
    paintings = Painting.objects.all()
    # Randomize order of paintings
    shuffled_paintings = list(paintings)
    random.shuffle(shuffled_paintings)
    return render(request, 'gallery.html', {'paintings': shuffled_paintings})

def painting(request, painting_name):
    painting = get_object_or_404(Painting, id=painting_name)
    return render(request, 'painting.html', {'painting': painting})