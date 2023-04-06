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

def contact(request):
    return render(request, 'contact.html')



#quotes for paitings page
quotes = [
'“Be content with what you have, rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you” -Lao Tzu',
'"Color is a power which directly influences the soul" -W. Kandinsky',
'"Every child is an artist. The problem is how to remain an artist once he grows up" -Pablo Picasso',
'“Better a diamond with a flaw than a pebble without” -Confucius',

]

def painting(request, painting_name):
    painting = get_object_or_404(Painting, title=painting_name)
    return render(request, 'painting.html', {'painting': painting, 'quote': random.choice(quotes)})