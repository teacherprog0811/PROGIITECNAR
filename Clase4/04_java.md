## Condicionales



### If Condition



```java
//Sintaxis
if condicion{
    codigo
} 
```

**Ejemplo: 1**

```java
int a = 3
if (a > 0){
    System.out.print("A es un numero positivo");
}
```

Como puede ver en el ejemplo anterior, 3 es mayor que 0. La condición era verdadera y se ejecutó el código del bloque. Sin embargo, si la condición es falsa, no vemos el resultado. Para ver el resultado de la condición falsa, debemos tener otro bloque, que va a ser _else_.

### If Else

Si la condición es verdadera se ejecutará el primer bloque, si no lo es se ejecutará la condición else.

```java
if (condicion){
    codigo
}else{
    codigo
}
```

**Ejemplo: **

```java
int a = 3
if (a < 0){
    System.out.println("Es un numero positivo");
}else{
    System.out.println("Es un numero negativo");
}
```

### Condiciones anidadas

Las condiciones pueden anidarse

```java
if (condicion){
    System.out.println("Entre en la primera condicion");
    if(condicion2){
        System.out.println("Entre en la segunda condicion");
    }
}else{
    System.out.println("Me fui en el else de la primera condicion");
}
```