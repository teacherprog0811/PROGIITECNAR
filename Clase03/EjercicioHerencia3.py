class Person:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def printname(self):
    print(self.nombre, self.apellido)

class Student(Person):
  def __init__(self, nombre, apellido,asignatura,nota1):
    super().__init__(nombre, apellido)
    self.asignatura = asignatura
    self.nota1 = nota1

x = Student("Ivan", "Narvaez","PROG2", "5")
print (f'El estudiante {x.nombre} {x.apellido} cursa {x.asignatura} y tiene una nota {x.nota1}')

