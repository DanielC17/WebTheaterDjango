from django.shortcuts import render
from WebTheater.model.categoria import Categoria
from WebTheater.model.video import Video




def index(request):
    return render(request, 'index.html')


