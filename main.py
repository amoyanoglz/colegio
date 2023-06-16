from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas = []
profesores = []

CANTIDAD = {
    "aulas": 5,
    "profesores": 7,
    "alumnos": 30
}

for i in range(CANTIDAD["aulas"]):
    aulas.append(Aula())

for i in range(CANTIDAD["profesores"]):
    profesores.append(Profesor())

for i in range(CANTIDAD["aulas"]):
    aulas[i].set_profesor(profesores[i % len(profesores)])

for i in range(CANTIDAD["alumnos"]):
    aulas[i % len(aulas)].add(Alumno())

for aula in aulas:
    print(f"cantidad alumnos {len(aula.alumnos)}")
    if aula.profesor != None:
        aula.puntuar()
        aula.listar()
        print()
        print(f"CONVOCADOS: ")
        aula.convocar_examen("A")
        print("##############################################")
        print()
    else:
        print("aula sin profesor")
