class Sesion:
    
    def __init__(self, id, nombre_asignatura, nombre_profesor, sala, fecha, hora_inicio, hora_fin, camara_en_uso, lista_camaras):
        self.id = id
        self.nombre_asignatura = nombre_asignatura
        self.nombre_profesor = nombre_profesor
        self.sala = sala
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.camara_en_uso = camara_en_uso
        self.lista_camaras = lista_camaras

    def iniciar_transmision(self):
        self.camara_en_uso.transmitir()

    def terminar_transmision(self):
        pass

    def cambiar_camara(self):
        index = self.lista_camaras.index(self.camara_en_uso)
        if index == len(self.lista_camaras) - 1:
            self.camara_en_uso = self.lista_camaras[0]
        else:
            self.camara_en_uso = self.lista_camaras[index + 1]