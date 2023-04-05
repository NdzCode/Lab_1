from Dispositivo import Dispositivo
from Sesion import Sesion

class Main(Sesion):

    def __init__(self):
        super().__init__(self)
       
        self.lista_sesiones = []

    def crear_sesion(self):
        id = input("Ingrese el ID de la sesión: ")
        nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
        nombre_profesor = input("Ingrese el nombre del profesor: ")
        sala = input("Ingrese el número de la sala: ")
        fecha = input("Ingrese la fecha de la sesión (dd/mm/yyyy): ")
        hora_inicio = input("Ingrese la hora de inicio de la sesión (hh:mm): ")
        hora_fin = input("Ingrese la hora de término de la sesión (hh:mm): ")
        cantidad_camaras = int(input("Ingrese la cantidad de cámaras disponibles en la sala: "))
        lista_camaras = []
        for i in range(cantidad_camaras):
            id_camara = input(f"Ingrese el ID de la cámara {i+1}: ")
            nombre_camara = input(f"Ingrese el nombre de la cámara {i+1}: ")
            resolucion_camara = input(f"Ingrese la resolución de la cámara {i+1}: ")
            marca_camara = input(f"Ingrese la marca de la cámara {i+1}: ")
            modelo_camara = input(f"Ingrese el modelo de la cámara {i+1}: ")
            camara = Dispositivo(id_camara, nombre_camara, resolucion_camara, marca_camara, modelo_camara)
            lista_camaras.append(camara)

        # evaluando
        #return lista_camaras and self.lista_sesiones[id,nombre_asignatura,nombre_profesor,sala,fecha,hora_inicio,hora_fin,cantidad_camaras,]
        
        
        # mejoras
        def iniciar_transmision():
            pass
        def cambiar_camara(self):
            pass
        def terminar_transmision():
            pass




    
    




if __name__=="__main__":
    pass
Sesion= Main()
Sesion.crear_sesion()
Sesion.cambiar_camara()





