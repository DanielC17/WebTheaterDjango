from WebTheater.model.video import Video

class Categoria:
    def __init__(self, id, titulo, descricao, img_url, list_video: list[Video]):
        self.id = id 
        self.titulo = titulo
        self.descricao = descricao
        self.img_url = img_url
        self.list_video = list_video


    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id 

    
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo


    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self):
        self.descricao = descricao

    
    def get_img_url(self):
        return self.img_url

    def set_img_url(self, img_url):
        self.img_url = img_url

    
    def get_list_video(self):
        return self.list_video

    def set_list_video(self, video):
        self.list_video.append(video)