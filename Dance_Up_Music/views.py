from django.shortcuts import render
from django.http import HttpResponse

posts = []
# Create your views here.
def home(request):
    context = {'posts': posts}
    # now the context is accessible within the template home.html
    return render(request, 'Dance_Up_Music/home.html', context)
