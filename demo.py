class cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado **2

lado = int(input("ingresa el lado"))

mi_cuadrado = cuadrado(lado)
r = mi_cuadrado.area()
print(f"el area es: {r}")

