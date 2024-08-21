class Lote:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def calculararea(self):
        print (self.largo * self.ancho)


class Casa(Lote):
    def __init__(self, largo, ancho, propietario):
        super().__init__(largo, ancho)
        self.propietario = propietario

    def printpropietario(self):
        print(self.propietario)


x = Casa(7,45,"Ivan Narvaez")
x.calculararea()
x.printpropietario()