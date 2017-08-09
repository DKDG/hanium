from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Restaurant
from .forms import PostModelForm
# Create your views here.

def main(request):
    qs = Restaurant.objects.all()
    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(location__icontains=query)
        qs = qs.filter(condition)
    return render(request, 'food/main.html', {
        'rest_list': qs,
        'query': query,
    })

def about(request):
    return render(request, 'food/about.html')

def service(request):
    return render(request, 'food/service.html')

def contact(request):
    return render(request, 'food/contact.html')

def post_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'food/post_detail.html', {'restaurant': restaurant})