import request_example

class Alumno:

    def __init__(self, nombre = None, turno = "A", correo =None):
        
        my_user = request_example.generate_name_and_email()[0]

        self.nombre = nombre if nombre is not None else my_user['nombre']
        self.correo = correo if correo is not None else my_user['correo']
        self.turno = "A"
        self.nota = 0

    def setNota(self, nota):
        self.nota = nota

    def describe(self):
        print(f"Alumno: {self.nombre.ljust(8)}", end = " - ")
        print(f"Turno:  {self.turno}", end = " - ")
        print(f"Nota:   {self.nota}")

    def convocar_examen(self, turno):
        if self.nota >= 5:
            print(f"Estimado/a {self.nombre}, su nota media ha sido un {self.nota} ha sivo vd convocado examen")
            print(f"{self.correo}")


