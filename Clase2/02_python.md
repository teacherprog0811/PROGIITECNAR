## Funciones

¿Qué es una función? Antes de comenzar a crear funciones, aprendamos qué es una función y por qué las necesitamos.

### Definicion

Una función es un bloque reutilizable de código o declaraciones de programación diseñadas para realizar una determinada tarea. Para definir o declarar una función, Python proporciona la palabra clave _def_. La siguiente es la sintaxis para definir una función. El bloque de funciones de código se ejecuta solo si se llama o invoca la función.

### Declarando y llamando una funcion

Cuando creamos una función, la llamamos declarar una función. Cuando comenzamos a usarlo, lo llamamos *llamar* o *invocar* una función. La función se puede declarar con o sin parámetros.

```py
# sintaxis
# Declarando una funcion
def nombre_funcion():
    codigo
    ccodigo
# Llamando una funcion
nombre_funcion()
```

### Funciones sin parametros

Una funcion puede ser declarada sin parametros.

**Ejemplo:**

```py
def imprimir_nombre ():
    nombre = 'Ivan'
    apellido = 'Narvaez'
    espacio = ' '
    nombrecompleto = nombre + espacio + apellido
    print(nombrecompleto)
imprimir_nombre () # Llamando una funcion

def suma ():
    num1 = 11
    num2 = 22
    total = num1 + num2
    print(total)
suma()
```

### Funciones retornando un valor - Parte 1

La función también puede devolver valores; si una función no tiene una declaración de devolución, el valor de la función es Ninguno. Reescribamos las funciones anteriores usando return. De ahora en adelante, obtenemos un valor de una función cuando la llamamos y la imprimimos.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Funciones con parametros

En una función podemos pasar diferentes tipos de datos (número, cadena, booleano, lista, tupla, diccionario o conjunto) como parámetro

- Parámetro único: si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento

```py
# sintaxis
# Declarando una funcion
def nombre_funcion(parametro):
    codigo
    ccodigo
# Llamando una funcion
nombre_funcion(parametro)
```

**Ejemplo:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Dos parámetros: una función puede tener o no un parámetro o parámetros. Una función también puede tener dos o más parámetros. Si nuestra función toma parámetros, deberíamos llamarla con argumentos. Comprobemos una función con dos parámetros:

```py
  # sintaxis
  # Declarando una función
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
```

**Ejemplo:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # el valor debe cambiarse a una cadena primero
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Pasar argumentos con clave y valor

Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

```py
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # el orden de los argumentos no importa aquí
```

**Ejemplo:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

### Función que devuelve un valor - Parte 2

Si no devolvemos un valor con una función, entonces nuestra función devuelve _None_ de forma predeterminada. Para devolver un valor con una función usamos la palabra clave _return_ seguida de la variable que estamos devolviendo. Podemos devolver cualquier tipo de datos desde una función.

- Devolviendo una cadena:
**Ejemplo:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- Devolviendo un numero:

**Ejemplo:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

- Devolviendo un booleano:
  **Example:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Devolviendo una lista:
  **Example:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Funcion con valos por defecto en los parametros

A veces pasamos valores predeterminados a los parámetros cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.

```py
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

**Ejemplo:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

### Número arbitrario de argumentos

Si no sabemos la cantidad de argumentos que pasamos a nuestra función, podemos crear una función que pueda tomar una cantidad arbitraria de argumentos agregando \* antes del nombre del parámetro.

```py
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

**Ejemplo:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Número predeterminado y arbitrario de parámetros en funciones

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
```

### Función como parámetro de otra función

```py
#Puedes pasar funciones como parámetros
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```