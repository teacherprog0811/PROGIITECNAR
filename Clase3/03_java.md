## Herencia en JAVA
La Herencia es uno de los 4 pilares de la programación orientada a objetos junto con la Abstracción, Encapsulación y Polimorfismo. Hay 3 palabras reservadas "nuevas" como son "extends", "protected" y "super".

● extends: Esta palabra reservada, indica a la clase hija cuál va a ser su clase padre, es decir, de qué clase va a heredar tanto sus atributos como sus métodos. Una clase en JAVA puede extender a una única clase. Sin embargo, podemos tener todos los niveles de Herencia que necesitemos.

● protected: sirve para indicar un tipo de visibilidad de los atributos y métodos de la clase padre y significa que cuando un atributo es 'protected' o protegido, solo es visible ese atributo o método desde una de las clases hijas y no desde otra clase.

● super: se utiliza para hacer referencia a la clase padre o a la superclase. Nos permite en la definición de una clase hija, acceder a los atributos y métodos de la clase padre. El uso más común es para llamar a un constructor de la clase padre desde el constructor de la clase hija, en ese caso la llamada deberá ser la primera instrucción del método.


## Ejemplo de Herencia

```java
public class Padre{
  String nombre;
  public Padre(String nombre){
    this.nombre = nombre;
    System.out.println(nombre);
  }
}

public class Hija extends Padre{
  int edad;
  public Hija(String nombre, int edad){
    super(nombre, edad);
    this.edad = edad;
    System.out.println("Tiene una hija de" + edad + "anios");
  }
}
```
