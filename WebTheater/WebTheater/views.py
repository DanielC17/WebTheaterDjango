from django.shortcuts import render
from WebTheater.model.categoria import Categoria
from WebTheater.model.video import Video

#Comedia
video1 = Video(1, "Thiago Ventura", "Comedia", "thg.png", 'https://www.youtube.com/embed/8KScgFZRbeM', '1 de fev. de 2022', 9000, "1.122.044 visualizações")
video2 = Video(2, "Afonso Padilha", "Comedia", "afonso.png", 'https://www.youtube.com/embed/0OJiQhxZpbw', '28 de mar. de 2022', 400 , "879.491 visualizações")

#Romance
video3 = Video(3, "Até a proxmia Vez", "Romance", "prx.jpg", 'https://www.youtube.com/embed/EtNYZvM6Utc', '3 de jan. de 2022', 8000, "100.195 visualizações")
video4 = Video(4, "Ainda Estou Aqui", "Romance", "aindaestouaq.jpg", 'https://www.youtube.com/embed/PqpnpPAaA48', '18 de mar. de 2022', 720000, "72.195 visualizações")

#Terror
video5 = Video(5,"Massacre da Serra Eletrica", "Terror", "massacre.jpg", "https://www.youtube.com/embed/v0GbEX98RF8", "31 de jan. de 2022", 60000, "604.388 visualizações")
video6 = Video(6, "A Entidade", "Terror", "entidade.jpg", "https://www.youtube.com/embed/-Q_dwLGd2Rs", "31 de jul. de 2021", 649,"91.106 visualizações")

# Tipo Categorias
categoria1 =Categoria(1, "Comedia", "Para rir", "comedia.jpg", [video1, video2])
categoria2 =Categoria(2, "Romance", "Para Amar", "romance.jpg", [video3, video4])
categoria3 =Categoria(2, "Terror", "Para dar Medo", "terror.jpg", [video5, video6])

categorias = [categoria1, categoria2, categoria3]




def index(request):
    return render(request, 'index.html', {'lista_ctg':categorias})


def video(request, id):
    for categoria in categorias:
        for video in categoria.get_list_video():
            if video.get_id() == int(id):
                return render(request, 'videos.html', {'video': video})
