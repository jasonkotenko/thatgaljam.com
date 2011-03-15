from django import forms
from django.forms import Textarea

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200)
    sender = forms.EmailField(label='Your e-mail')
    message = forms.CharField(widget=Textarea())
    cc_myself = forms.BooleanField(required=False)
    
