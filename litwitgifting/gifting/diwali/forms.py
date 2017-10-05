from django import forms
from django.contrib import auth
from models import *
from django.forms.extras.widgets import SelectDateWidget

class contactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'5000','id':'name','placeholder':'Name', 'required data-validation-required-message':'Please enter your name.'}),required=True)
    phone = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'type': 'number','class': 'form-control','min':'0','id':'phone','placeholder':'Phone',}))
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','id':"email", 'type':"email", 'placeholder':"Email Address", 'required data-validation-required-message':"Please enter your email address."}))
    query = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows': '3','maxlength':'5000','id':"message", 'placeholder':"Message",'data-validation-required-message':"Please enter a message."}),required=True)
    class Meta:
        fields = ('name','phone','email','query')
        model = ContactUs

