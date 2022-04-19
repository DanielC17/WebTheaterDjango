from django.shortcuts import render
from WebTheater.model.categoria import Categoria
from WebTheater.model.video import Video

video1 = Video(1, "Thiago Ventura", "StandUp", "thg.png", 'https://www.youtube.com/embed/8KScgFZRbeM', '1 de fev. de 2022', 9000, "1.122.044 visualizações")
video2 = Video(2, "Afonso Padilha", "StandUp", "afonso.png", 'https://www.youtube.com/embed/0OJiQhxZpbw', '28 de mar. de 2022', 400 , "879.491 visualizações")

video3 = Video(3, "Thiago Ventura", "StandUp", "th.jpg", 'video_url', '19/04/2022', 90000, 300000)
video4 = Video(4, "Thiago Ventura", "StandUp", "th.jpg", 'video_url', '19/04/2022', 90000, 300000)



categoria1 =Categoria(1, "Comedia", "Para rir", "comedia.jpg", [video1, video2])
categoria2 =Categoria(2, "Romance", "Para Amar", "romance.jpg", [video3, video4])
categoria3 =Categoria(2, "Terror", "Para dar Medo", "terror.jpg", [])

categorias = [categoria1, categoria2, categoria3]




def index(request):
    return render(request, 'index.html', {'lista_ctg':categorias})


def video(request, id):
    for categoria in categorias:
        for video in categoria.get_list_video():
            if video.get_id() == int(id):
                return render(request, 'videos.html', {'video': video})
