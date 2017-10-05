from django.shortcuts import render
from forms import *
# Create your views here.

def indexView(request):
    dictV = {}
    dictV['form'] = contactForm()

    return render(request,'gifting.html',dictV)

#Contact Us
def contactUs(request):
    dictV = {}
    dictV['form'] = contactForm()
    print request.method

    form = contactForm(request.POST)
    if form.is_valid():
       form.save()
       dictV['success'] = True
       print 'success'
    else:
       dictV['error'] = True
       print form.error
    print request.method
    print dictV
    return render(request,'gifting.html',dictV)

