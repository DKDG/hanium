from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'food/main.html')

def about(request):
    return render(request, 'food/about.html')

def service(request):
    return render(request, 'food/service.html')

def contact(request):
    return render(request, 'food/contact.html')