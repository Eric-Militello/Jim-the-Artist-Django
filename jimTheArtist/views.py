from django.shortcuts import render
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