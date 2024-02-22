class Person:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def printname(self):
    print(self.nombre, self.apellido)

class Student(Person):
  def __init__(self, nombreE, apellidoE):
    super().__init__(nombreE, apellidoE)
    self.graduacion = 2019

x = Student("Ivan", "Narvaez")
print("El estudiante", x.nombre, x.apellido, "Se graduo el año", x.graduacion)
