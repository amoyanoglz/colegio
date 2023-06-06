import random
from alumno import Alumno


class Aula:

    def __init__(self):
        self.alumnos = []
    

    def add(self, alumno):
        self.alumnos.append(alumno)

    def listar(self):
        for i in self.alumnos:
            i.setNota(random.randint(0,10))
            i.describe()

    def convocarExamen(self, turno):
        for x in self.alumnos:
            x.convocarExamen(turno)
        # setVacio(False)
        
        # if self.vacio == True:
        #     print("ni el taro")

