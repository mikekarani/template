from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,  'about  us.html')

def contact(request):
    return render(request,  'contact.html')


def gallery(request):
    return render(request,  'gallery.html')

def service(request):
    return render(request,  'services.html')


