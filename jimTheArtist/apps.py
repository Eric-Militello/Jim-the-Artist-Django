from django.apps import AppConfig
from django import forms


class JimtheartistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jimTheArtist'

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Your Message', widget=forms.Textarea(attrs={'class': 'form-control'}))
