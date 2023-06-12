import random
import profesor

class Aula:
    def __init__(self):
        self.alumnos = []
        self.profesor = None
    
    def add(self, alumno):
        self.alumnos.append(alumno)
    
    def listar(self):
        if self.profesor == None:
            pass
            # raise Exception(f'esta clase tiene profesor')
        else:
            # print(f"PROFESOR: {self.profesor}")
            self.profesor.describe_profe()
            for alumno in self.alumnos:
                alumno.describe()
        
    
    def convocar_examen(self, turno):
        # print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.convocar_examen(turno)

    def convocar_examen_all(self):
        pass

    def puntuar(self):
        if self.profesor != None:
            for alumno in self.alumnos:
                alumno.setNota(self.profesor.generar_nota())
                # alumno.describe()
    
    def set_profesor(self, profesor):
        self.profesor = profesor

