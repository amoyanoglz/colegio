from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas = []
profesores = []

CANTIDAD = {
    "aulas": 5,
    "profesores": 3,
    "alumnos": 14
}


for i in range(CANTIDAD["aulas"]):
    aulas.append(Aula())

# print(aulas)
# print(len(aulas))


profesores = []

for i in range(CANTIDAD["profesores"]):
    profesores.append(Profesor())
# profesores = [
#     Profesor("Juanito Balerrama", 0, 10),
#     Profesor("Carmen Lapido", 3, 7),
#     Profesor("Dolores Lola", 2, 9)
# ]

# aulas[0].set_profesor(profesores[0])
# aulas[1].set_profesor(profesores[0])
# aulas[2].set_profesor(profesores[0])
# aulas[3].set_profesor(profesores[0])
# aulas[4].set_profesor(profesores[0])


for i in range(CANTIDAD["aulas"]):
    # print("veo i del forde proifes")
    # print(i)
    # print("veo del modulo")
    # print(i % len(profesores))
    aulas[i].set_profesor(profesores[i % len(profesores)])

for i in range(CANTIDAD["alumnos"]):
    aulas[i % len(aulas)].add(Alumno())

for aula in aulas:
    print(f"longitud alumnos {len(aula.alumnos)}")
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
