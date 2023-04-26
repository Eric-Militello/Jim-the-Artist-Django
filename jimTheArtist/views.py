from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
import random
from .models import Painting
from .apps import ContactForm

def home(request):
    return render(request, 'home.html')

def gallery(request):
    # Retrieve all active paintings from the database
    paintings = Painting.objects.filter(active=True)
    # Randomize order of paintings
    shuffled_paintings = list(paintings)
    #random.shuffle(shuffled_paintings)
    return render(request, 'gallery.html', {'paintings': shuffled_paintings})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # send the email
            try:
                # send the email
                send_mail(
                    f"New message from {name} ({email})",
                    message,
                    email,
                    ['ericmilitellocoding@gmail.com'],
                    fail_silently=False,
                )
                # add a success message
                # clear the form fields
                form = ContactForm()
                messages.success(request, 'Your message was successfully sent!')
            except Exception as e:
                # add an error message
                messages.error(request, 'There was an error sending your message. Please try again later.')

            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



#quotes for paitings page
quotes = [
'“Be content with what you have, rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you” -Lao Tzu',
'"Color is a power which directly influences the soul" -W. Kandinsky',
'"Every child is an artist. The problem is how to remain an artist once he grows up" -Pablo Picasso',
'“Better a diamond with a flaw than a pebble without” -Confucius',

]

def painting(request, painting_name):
    painting = get_object_or_404(Painting, title=painting_name)
    #price value of 0 painting is sold. less than 0 represents a painting is not for sale
    if painting.price == 0:
        painting.price = 'Sold'
    elif  painting.price < 0:
        painting.price = 'Not For Sale'
    #add $ and commas for display
    else:
        painting.price = '${:,.0f}'.format(painting.price)


    #convert length and width from inches to cm for display
    length_cm = str(painting.length * 2.54) + 'cm'
    height_cm = str(painting.height * 2.54)  + 'cm'



    return render(request, 'painting.html', {'painting': painting,
                                             'quote': random.choice(quotes),
                                             'length_cm': length_cm,
                                             'height_cm': height_cm
                                             }
                                             )