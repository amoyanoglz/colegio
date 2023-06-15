import random
import request_example

class Profesor:
    def __init__(self, nombre = None, nota_minima = 3, nota_maxima = 9):

        my_user = request_example.generate_name_and_email()[0]

        VALID_NOTES = {
            "min": (0.0, 4.0),
            "max": (6.0, 10.0)
        }

        def validar_nota_minima(nota_minima):
            min = VALID_NOTES["min"][0]
            max = VALID_NOTES["min"][1]

            if nota_minima < min:
                raise Exception(f'La nota mínima debe ser superior a {min}')
            if nota_minima > max:
                raise Exception(f'La nota mínima debe ser inferior a {max}')

            return nota_minima

        def validar_nota_maxima(nota_maxima):
            min = VALID_NOTES["max"][0]
            max = VALID_NOTES["max"][1]

            if nota_maxima < min:
                raise Exception(f'La nota máxima debe ser superior a {min}')
            if nota_maxima > max:
                raise Exception(f'La nota máxima debe ser inferior a {max}')
            return nota_maxima

        self.nombre = nombre if nombre is not None else my_user['nombre']
        self.nota_minima = 3
        self.nota_maxima = 9
        # self.nota_minima = validar_nota_minima(nota_minima)
        # self.nota_maxima = validar_nota_maxima(nota_maxima)

    # def __str__(self) -> str:
    #     return f"{self.nombre} [{self.nota_minima}/{self.nota_maxima}]"

    def generar_nota(self) -> float:
        if self.nombre != None:
            return round((random.uniform(self.nota_minima, self.nota_maxima)), 2)
        else:
            print("no profe, no nota")

    def describe_profe(self):
        print(f"Profesor: {self.nombre}")
        print(f"nota mininma: {self.nota_minima}")
        print(f"nota maxima: {self.nota_maxima}")
