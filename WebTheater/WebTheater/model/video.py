class Video:
    
    def __init__(self, id, titulo, descricao, img_url, video_url, data_publicacao, qtd_curtida, qtd_visualizacao):
        self.id = id
        self.titulo = titulo 
        self.descricao = descricao
        self.img_url = img_url
        self.video_url = video_url
        self.data_publi = data_publi
        self.qtd_curtida = qtd_curtida
        self.qtd_visualizacao = qtd_visualizacao
        


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

    def set_descricao(self, descricao):
        self.descricao


    def get_img_url(self):
        return self.img_url

    def set_img_url(self, img_url):
        self.img_url = img_url


    def get_video_url(self):
        return self.video_url

    def set_video_url(self, video_url):
        self.video_url = video_url


    def get_data_publi(self):
        return self.data_publi

    def set_data_publi(self, data_publi):
        self.data_publi = data_publi
    

    def get_qtd_curtida(self):
        return self.qtd_curtida

    def set_qtd_curtida(self, qtd_curtida):
        self.qtd_curtida = qtd_curtida


    def get_qtd_visualizacao(self):
        return qtd_visualizacao

    def set_qtd_visualizacao(self, qtd_visualizacao):
        self.qtd_visualizacao = qtd_visualizacao    


