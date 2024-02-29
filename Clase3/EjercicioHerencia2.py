class Person:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def printname(self):
    print(self.nombre, self.apellido)

class Student(Person):
  def __init__(self, nombre, apellido):
    Person.__init__(self, nombre, apellido)

x = Student("Ivan", "Narvaez")
x.printname()
