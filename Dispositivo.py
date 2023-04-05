from Camara import Camara

class Dispositivo(Camara):

    def __init__(self,id,nombre,resolucion,marca,modelo):
        super().__init__(id,nombre,resolucion)
        self.__marca = marca
        self.__modelo = modelo



    def transmitir(self):
        return f'tramsmitiendo desde {self.nombre}'



    
