class cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado **2

micuadrado = cuadrado(5)
print("el area es: ", micuadrado.area())

