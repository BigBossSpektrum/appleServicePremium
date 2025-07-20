from django.shortcuts import render

# Create your views here.

def base_view(request):
    """Vista para mostrar la plantilla base.html"""
    return render(request, 'base.html')

def about_view(request):
    """Vista para mostrar la plantilla about.html"""
    return render(request, 'about.html')

def contact_view(request):
    """Vista para mostrar la plantilla contact.html"""
    return render(request, 'contact.html')