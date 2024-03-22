## Condicionales

Por defecto, las sentencias en un script Python se ejecutan secuencialmente de arriba a abajo. Si la lógica de procesamiento lo requiere, el flujo secuencial de ejecución puede alterarse de dos maneras:

- Ejecución condicional: un bloque de una o más sentencias se ejecutará si una determinada expresión es verdadera
- Ejecución repetitiva: un bloque de una o más sentencias se ejecutará repetidamente mientras cierta expresión sea verdadera. En esta sección, cubriremos las sentencias _if_, _else_, _elif_. Los operadores lógicos y de comparación que aprendimos en secciones anteriores serán útiles aquí.

### If Condition

En python y otros lenguajes de programación se utiliza la palabra clave _if_ para comprobar si una condición es verdadera y ejecutar el código del bloque. Recuerda la sangría después de los dos puntos.

```py
# syntax
if condicion:
    codigo
```

**Example: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A es un numero positivo
```

Como puede ver en el ejemplo anterior, 3 es mayor que 0. La condición era verdadera y se ejecutó el código del bloque. Sin embargo, si la condición es falsa, no vemos el resultado. Para ver el resultado de la condición falsa, debemos tener otro bloque, que va a ser _else_.

### If Else

Si la condición es verdadera se ejecutará el primer bloque, si no lo es se ejecutará la condición else.

```py
# syntax
if condicion:
    codigo
else:
     codigo
```

**Ejemplo: **

```py
a = 3
if a < 0:
    print('A es un numero negativo')
else:
    print('A es un numero positivo')
```

La condición anterior resulta falsa, por lo que se ejecuta el bloque else. ¿Qué pasa si nuestra condición es más de dos? Podríamos utilizar _ elif_.

### If Elif Else

En nuestra vida cotidiana, tomamos decisiones a diario. No tomamos decisiones comprobando una o dos condiciones, sino múltiples condiciones. Al igual que en la vida, la programación también está llena de condiciones. Usamos _elif_ cuando tenemos múltiples condiciones.

```py
# syntax
if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo

```

**Ejemplo: **

```py
a = 0
if a > 0:
    print('A es un numero positivo')
elif a < 0:
    print('A es un numero negativo')
else:
    print('A es cero')
```


### Condiciones anidadas

Las condiciones pueden anidarse

```py
# syntax
if condicion:
    codigo
    if condicion:
    codigo
```

**Ejemplo: **

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A es un número entero positivo y par')
    else:
        print('A es un número positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es un número negativo')

```

Podemos evitar escribir condiciones anidadas utilizando el operador lógico _and_.

### Condición If y operadores lógicos

```py
# syntax
if condition and condition:
    code
```

**Example: **

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A es un número entero par y positivo')
elif a > 0 and a % 2 !=  0:
     print('A es un número entero positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es negativo')
```

### Operadores lógicos If y Or

```py
# syntax
if condition or condition:
    code
```

**Example: **

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Acceso concedido!')
else:
    print('Acceso denegado!')
```