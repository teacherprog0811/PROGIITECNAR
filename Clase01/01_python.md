### Tipos de datos

En Python existen varios tipos de tipos de datos. Comencemos con los más comunes. Los diferentes tipos de datos se cubrirán en detalle en otras secciones. Por el momento, repasemos los diferentes tipos de datos y familiaricémonos con ellos. No es necesario que tengas una comprensión clara ahora.

#### Numero

- Integer: Integer(negativo, cero and positivo) numeros
    Ejemplo:
    ... -3, -2, -1, 0, 1, 2, 3 ...
- Float: Decimal number
    Ejemplo
    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex
    Ejemplo
    1 + j, 2 + 4j

#### String

Una colección de uno o más caracteres bajo comillas simples o dobles. Si una cadena tiene más de una oración, usamos comillas triples.

**Ejemplo:**

```py
'Tecnar'
"Programacion"
'Yo soy un estudiante de programacion con python de Tecnar'
```

#### Booleans

Un tipo de datos booleano es un valor Verdadero o Falso. T y F siempre deben estar en mayúsculas.

**Ejemplo:**

```python
    True  
    False 
```

### Verificando Tipos de datos

Para verificar el tipo de datos de ciertos datos/variables utilizamos la función **tipo**. En la siguiente terminal verá diferentes tipos de datos de Python:

![Checkeando tipos de datos](../images/checking_data_types.png)

### Archivo de Python

Primero abra la carpeta de su proyecto, Si no tiene esta carpeta, cree un nombre de carpeta. Dentro de esta carpeta, cree un archivo llamado `helloworld.py`. Ahora, hagamos lo que hicimos en el shell interactivo de Python usando el código de Visual Studio.

El shell interactivo de Python se estaba imprimiendo sin usar **print** pero en el código de Visual Studio para ver nuestro resultado deberíamos usar una función incorporada _print(). La función incorporada _print()_ toma uno o más argumentos de la siguiente manera _print('arument1', 'argument2', 'argument3')_. Vea los ejemplos a continuación.


**Ejemplo:**

El archivo llamado helloworld.py

```py

print(2 + 3)             # suma(+)
print(3 - 1)             # resta(-)
print(2 * 3)             # multiplicacion(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponencial(**)
print(3 % 2)             # modulo(%)
print(3 // 2)            # Redondear divisiones(//)

# Verificando los tipos de datos
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
```