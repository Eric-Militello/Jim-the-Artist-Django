from django.apps import AppConfig
from django import forms


class JimtheartistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jimTheArtist'

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)