from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request, 'navigation/About.html')
def Contact(request):
    return render(request, 'navigation/Contact.html')

