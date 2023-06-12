from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas = [Aula(), Aula(), Aula(), Aula(), Aula(), Aula(), Aula()]

profesores = [
        Profesor("Juanito Balerrama", 0, 10),
        Profesor("Carmen Lapido", 3, 7),
        Profesor("Dolores Lola", 2, 9)
]

aulas[0].set_profesor(profesores[0])
aulas[0].add(Alumno("Pepito", "A", "pepito@a.com"))
aulas[0].add(Alumno("Lucia", "A", "lucia@a.com"))
aulas[0].add(Alumno("Martita", "A", "martita@b.com"))
aulas[0].add(Alumno("Gloria", "A", "gloria@b.com"))
aulas[0].add(Alumno("Juanito", "A", "juanito@c.com"))
aulas[0].add(Alumno("Jorgito", "A", "jorgito@c.com"))
aulas[0].add(Alumno("Jaimito", "A", "jaimito@c.com"))

aulas[1].set_profesor(profesores[1])
aulas[1].add(Alumno("Marcos", "A", "marcos@a.com"))
aulas[1].add(Alumno("Antonio", "A", "antonio@a.com"))

aulas[2].set_profesor(profesores[2])
aulas[2].add(Alumno("Carmen", "A", "carmens@a.com"))
aulas[2].add(Alumno("Lucia", "A", "lucia@a.com"))

aulas[3].set_profesor(profesores[0])
aulas[3].add(Alumno("Marcos", "B", "marcos@b.com"))
aulas[3].add(Alumno("Antonio", "B", "antonio@b.com"))

aulas[4].set_profesor(profesores[1])
aulas[4].add(Alumno("Karin", "B", "karin@b.com"))
aulas[4].add(Alumno("Nolito", "B", "nolito@b.com"))

# aulas[5].set_profesor(profesores[1])
aulas[5].add(Alumno("Marcos", "A", "marcos@a.com"))
aulas[5].add(Alumno("Antonio", "A", "antonio@a.com"))

aulas[6].set_profesor(profesores[2])
# aulas[5].add(Alumno("Marcos", "A", "marcos@a.com"))
# aulas[5].add(Alumno("Antonio", "A", "antonio@a.com"))

for aula in aulas:
    # print(aula.profesor)
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
        print("aulsin profesor")
    
# def convocatiaria_general():
#     print("CONVOCATORIA GENERAL: ")
#     for i in aulas:
#         i.convocar_examen_all()

# convocatiaria_general()

# mi_aula5.set_profesor(mi_profe1)
# mi_aula5.add(Alumno("Antoine", "C", "antonine@c.com"))
# mi_aula5.add(Alumno("Molina", "C", "molina@c.com"))


# print("CONVOCADOS AULA0:")
# mi_aula.convocar_examen("A")


# print("CONVOCADOS AULA1:")
# mi_aula1.convocar_examen("A")

# mi_aula2.puntuar()
# mi_aula2.listar()
# print()
# print("CONVOCADOS AULA2:")
# mi_aula2.convocar_examen("A")

# mi_aula3.puntuar()
# mi_aula3.listar()
# print()
# print("CONVOCADOS AULA3:")
# mi_aula1.convocar_examen("B")

# mi_aula4.puntuar()
# mi_aula4.listar()
# print()
# print("CONVOCADOS AULA4:")
# mi_aula1.convocar_examen("B")
