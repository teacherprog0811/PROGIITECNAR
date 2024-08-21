## Arreglos

Un arreglo es un objeto que contiene un conjunto de variables del mismo tipo en su interior. La cantidad de elementos que tiene un arreglo es estatica, fija y se define en el momento de su declaracion y no se puede podificar.

El indice del primer elemento es cero y el ultimo es la cantidad de elementos menos uno.

### Como crear un arreglo

En Java podemos crear arreglos y listas de arreglos para ello podemos hacerlo de la siguiente manera:

```java
// Enteros
int a [];
ArrayList<Integer> arrList = new ArrayList();
// Cadena
String [] cadena;
ArrayList<String> list = new ArrayList();    
// Double
Double [] ejemplo;
ArrayList<Double> arrList = new ArrayList();
```

```java
int ejemplo [] = new int[10];
```

### Asignando valores a un arreglo

- Forma 1
```java
int c[] = {1,2,3,4,5,6,7,8,9,10,11};
ArrayList<Integer> arrList = new ArrayList();  
arrList.add(0, 100);
```
- Forma 2
```java
int c2[] = new int[8];
c2[0] = 12;
c2[1] = 8;
```
### Recorriendo un arreglo 
```java
int c[] = {1,2,3,4,5,6,7,8,9,10,11};
System.out.println(c[0]); // Imprime el 1

//Ciclo para recorrer un arreglo
for (int i = 0;i<c.length;i++){
  System.out.println(c[i]);
}

// Utilizando foreach 
String paises[] = {"Colombia","Brazil","Argentina"};
for (String pais : paises){
  System.out.println(pais);
}
```

### Agregando elementos a un ArrayList con el metodo Add()

Para añadir un elemento al final de una lista existente utilizamos el método *add()*.

```java
import java.util.ArrayList;

public class Arreglos {

    public static void main(String[] args) {
        
        ArrayList<Integer> arrList = new ArrayList();
        arrList.add(0, 1); // Especificamos el indice y el valor a almacenar.
        arrList.add(1, 2);
        arrList.add(2, 3);
        System.out.println(arrList); // Salida [1, 2, 3]

    }
}
```

### Eliminando items de un ArrayList

El método remove elimina un elemento especificado de una lista

```java
import java.util.ArrayList;

public class Arreglos {

    public static void main(String[] args) {
        
        ArrayList<Integer> arrList = new ArrayList();
        arrList.add(0, 1); // Especificamos el indice y el valor a almacenar.
        arrList.add(1, 2);
        arrList.add(2, 3);
        
        arrList.remove(1); // Se especifica el index a eliminar
        System.out.println("Imprimiendo Lista despues de eliminacion" +arrList);

    }
}

```

### Limpiando Items de un ArrayList

El método *clear()* vacía la lista:

```java
 ArrayList<Integer> arrList = new ArrayList();
        arrList.add(0, 100);
        arrList.add(1, 200);
        arrList.add(2, 300);
        arrList.add(3, 400);
        arrList.add(4, 500);
        arrList.add(5, 600);
arrList.clear();
System.out.println("Imprimiendo Lista despues de vaciada" +arrList);
```

### Obtener el primer elemento de un ArrayList

Para obtener el primer elemento de la lista se utiliza el metodo getFirst().

```java
ArrayList<Integer> arrList = new ArrayList<Integer>();
        arrList.add(0, 1);
        arrList.add(1, 2);
        arrList.add(2, 3);
 System.out.println("Imprimiendo primer elemento GET " +arrList.get(0)); // Imprimir primer elemento con GET
 System.out.println("Imprimiendo primer elemento" +arrList.getFirst()); // Imprimir primer elemento con getFirst
```

### Obtener el ultimo elemento de un ArrayList

Para obtener el ultimo elemento de la lista se utiliza el metodo getLast().

```java
ArrayList<Integer> arrList = new ArrayList<Integer>();
        arrList.add(0, 1);
        arrList.add(1, 2);
        arrList.add(2, 3);
System.out.println("Imprimiendo primer elemento GET " +arrList.get(2)); // Imprimir el ultimo elemento con GET
System.out.println("Imprimiendo ultimo elemento" +arrList.getLast()); // Imprimir ultimo elemento con getLast
```

### Obtener el tamaño de un Arraylist

El método *size()* devuelve el tamaño de una lista.

```java
ArrayList<Integer> arrList = new ArrayList<Integer>();
        arrList.add(0, 1);
        arrList.add(1, 2);
        arrList.add(2, 3);
System.out.println("El tamaño de la lista es: " +arrList.size()); // Imprimira en pantalla 3
```


### Búsqueda de un elemento en un ArrayList

El método *contains()* devuelve verdadero o falso si un elemento esta en una lista:

```java
ArrayList<Integer> arrList = new ArrayList<Integer>();
        arrList.add(0, 1);
        arrList.add(1, 2);
        arrList.add(2, 3);
System.out.println("El valor 1 esta en la lista ? " +arrList.contains(1)); // Devolvera un verdadero en la consola.
```


### Invertir elementos de un ArrayList

El método *reversed()* invierte el orden de una lista.

```java
ArrayList<Integer> arrList = new ArrayList<Integer>();
        arrList.add(0, 100);
        arrList.add(1, 200);
        arrList.add(2, 300);
        arrList.add(3, 400);
        arrList.add(4, 500);
        arrList.add(5, 600);
System.out.println("Invirtiendo la lista:  " +arrList.reversed());

```

### Ordenando Elementos de un ArrayList

Para ordenar listas podemos utilizar el método sort() pero antes debemos importar la libreria Collections para poder ordenar nuestro arrayList.
 
- sort(): este método modifica la lista original

  ```java

  import java.util.ArrayList;
  import java.util.Collections;

  public class Arreglos {

      public static void main(String[] args) {
          
          ArrayList<Integer> arrList = new ArrayList();
          arrList.add(0, 100);
          arrList.add(1, 300);
          arrList.add(2, 400);
          arrList.add(3, 700);
          arrList.add(4, 500);
          arrList.add(5, 600);
          Collections.sort(arrList);
          System.out.println("Ordenando la lista:  " +arrList);
      }
  }
  ```
