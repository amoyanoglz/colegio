import request_example

class Usuario:

    def __init__(self, nombre = None, correo = None, turno = "A"):

        my_user = request_example.generate_name_and_email()[0]

        self.nombre = nombre if nombre is not None else my_user['nombre']
        self.correo = correo if correo is not None else my_user['correo']
        self.turno = "A"

    
    def __str__(self):
        return f"{self.nombre} {self.correo} {self.turno}"

    # def __del__(self):
    #     print(f"ha muerto el usuario {self.nombre}")


usuario1 = Usuario()

print(usuario1)
    