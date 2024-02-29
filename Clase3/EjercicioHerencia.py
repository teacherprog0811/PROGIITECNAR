class Person:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def printname(self):
    print(self.nombre, self.apellido)

class Student(Person):
  pass
#pass Declaracion nula
x = Student("Ivan", "Narvaez")
x.printname()