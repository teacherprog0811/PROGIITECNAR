class Person:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def printname(self):
    print(self.nombre, self.apellido)

class Student(Person):
  def __init__(self, nombre, apellido,edad):
    self.edad = edad
    Person.__init__(self, nombre, apellido)
  def printedad(self):
    print(self.edad)

x = Student("Ivan", "Narvaez",34)
x.printname()
x.printedad()
