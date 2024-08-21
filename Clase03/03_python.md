## Creacion de una clase en Python
Para la creacion de una clase en Python se utiliza la palabra reservada class seguido del nombre de la clase. Por ejemplo:

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
```
En el ejemplo anterior vemos como se define el constructor de la clase con la palabra reservada __init__ 

## Herencia en Python

¿ Que es La herencia ? nos permite definir una clase que hereda todos los métodos y propiedades de otra clase. La clase principal es la clase de la que se hereda, también llamada clase base. La clase hija es la clase que hereda de otra clase, también llamada clase derivada.

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()
```	

### Clase heredada

Para crear una clase que herede la funcionalidad de otra clase, envíe la clase principal como parámetro al crear la clase secundaria:

```python
class Student(Person):
  pass
```

