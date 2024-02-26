class Person:
  def __init__(self, firstname="Nombre", lastname="Apellido", age=0, country="Pais", city="Ciudad"):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city

  def Obtenerinfo(self):
    #Uso de f-string
    return f'{self.firstname} {self.lastname} tiene {self.age} años de edad y vive en {self.city}, {self.country}'
    #Uso de print anidado"
    #print("Mi nombre es", self.firstname, self.lastname,"tengo",self.age, "años de edad y vivo en", self.city, self.country)


