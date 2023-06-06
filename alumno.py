class Alumno:
    def __init__(self, nombre, turno, correo):
        self.nombre = nombre
        self.correo = correo
        self.turno = turno
        self.nota = 0

    def setNota(self, nota):
        self.nota = nota

    def describe(self):
        print(f"Alumnno: {self.nombre.ljust(8)}", end = " - ")
        print(f"Turno: {self.turno}", end = " - ")
        print(f"Nota: {self.nota}")

    def convocarExamen(self, turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"Alumnno: {self.nombre.ljust(8)}", end = " - ")
            print(f"Turno: {self.turno}", end = " - ")
            print(f"Nota: {self.nota}", end = " - ")
            print(f"{self.correo}", end = " - ")
            print(f"Estimado/a {self.nombre} su nota media ha sido {self.nota}")
            # setPp("BBB")
            # print(self.pp)
            # setVacio(False)
            # print(self.vacio)
            # print(f"estado de vacio es {vacio}")
 
