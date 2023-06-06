import random
from alumno import Alumno
from aula import Aula

turnos = ["A", "B", "C"]
aula = Aula()

aula.add(Alumno("Pepito", turnos[0], "pepito@a.com"))
aula.add(Alumno("Lucia", turnos[0], "lucia@a.com"))
aula.add(Alumno("Martita", turnos[1], "martita@a.com"))
aula.add(Alumno("Gloria", turnos[1], "gloria@a.com"))
aula.add(Alumno("Juanito", turnos[2], "juanito@a.com"))
aula.add(Alumno("Jorgito", turnos[2], "jorgito@a.com"))
aula.add(Alumno("Jaimito", turnos[2], "jaimito@a.com"))

aula.listar()
# vacio = True
turno_convocado = str(input("dime turno a convocar: "))
aula.convocarExamen(turno_convocado)


# alumnos = [
#     Alumno("Pepito", turnos[0], "pepito@a.com"),
#     Alumno("Lucia", turnos[0], "lucia@a.com"),
#     Alumno("Martita", turnos[1], "martita@a.com"),
#     Alumno("Gloria", turnos[1], "gloria@a.com"),
#     Alumno("Juanito", turnos[2], "juanito@a.com"),
#     Alumno("Jorgito", turnos[2], "jorgito@a.com"),
#     Alumno("Jaimito", turnos[2], "jaimito@a.com")
# ]

# for alumno in alumnos:
#     alumno.setNota(random.randint(3, 10))
#     alumno.describe()

# print()
# for turno in turnos:
#     print(f"TURNO: {turno}")
#     for convocado in alumnos:
#         convocado.convocarExamen(turno)
#     print("")

