## Funciones

¿Qué es una función? Antes de comenzar a crear funciones, aprendamos qué es una función y por qué las necesitamos.

### Definicion

Una función es un bloque reutilizable de código o declaraciones de programación diseñadas para realizar una determinada tarea. Para definir o declarar una función, JAVA proporciona la palabra clave function. La siguiente es la sintaxis para definir una función. El bloque de funciones de código se ejecuta solo si se llama o invoca la función.

### Declarando y llamando una funcion

El método es el mecanismo de subprogramación que ofrece el lenguaje JAVA. Un método se declara definiendo su cabecera y su cuerpo, dentro de una clase JAVA.

La cabecera de un método se define, en este orden:
● Acceso(modificadores de visibilidad y directiva static).
● Tipo de retorno, o tipo de sus resultados (valores de retorno).
● Nombre (identificador).
● Lista de parámetros, o los tipos y nombres de sus datos (parámetros).
El cuerpo es la secuencia de instrucciones que se ejecutan al invocarlo, puede incluir:
● Declaraciones de variables.
● Cualquier tipo de instrucción o bloque de instrucciones: asignación, condicional,
bucle, e incluso, llamadas o invocaciones a otros métodos.

[Declaracion de metodos JAVA](./images/declaracion_metodos_java.png)

### Funciones sin parametros

Una funcion puede ser declarada sin parametros.

**Ejemplo:**

```java
public class Test {
    public static void main (String args[]){
        System.out.print(Bienvenido());
    } 
    static String Bienvenido(){
        return ("Bienvenido al sistema");
    }
    
}

```

### Funciones con parametro

```java
public class Ejemplo {
public static void main (String args[])
{
int num = 5;
int numDoble = doble(num);
} //numDoble vale 10, pero num vale 5
static int doble(int a)
{
a = a*2;
return a;
}
}
```