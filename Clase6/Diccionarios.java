
import java.util.Dictionary;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

/**
 *
 * @author Ing. Narvaez Mejia
 */
public class Diccionarios {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        Dictionary persona = new Hashtable();
        
        persona.put("nombre", "Ivan");
        persona.put("apellido", "Narvaez");
        persona.put("Edad", "34");
        persona.put("Sexo", "Masculino");
        
        System.out.println("El objeto diccionario con Hashtable personas es: " +persona);
        
        
        Map<String, String> persona2 = new HashMap();
        
        //Agregando key y value al diccionario
        
        persona2.put("Nombre", "Dario");
        persona2.put("Apellido", "Mejia");
        persona2.put("Edad", "34");
        persona2.put("Sexo", "Masculino");
        
        System.out.println("El objeto diccionario con HashMap personas es: " +persona2);
        
        //Obteniendo valores del diccionario
        
        String nombre = persona2.get("nombre");
        
        System.out.println("Obteniendo valor del key nombre: " +nombre);
        
        //Eliminando un elemento del diccionario
        
        persona2.remove("nombre");
        
        System.out.println("Nuevo dict despues de eliminacion: " +persona2);
        
        //Obteniendo el tamaño del diccionario
        
        int t = persona2.size();
         
         System.out.println("El tamaño del diccionario es: " +t);
         
         //Busqueda en el diccionario por Key o por Value
         
         
         System.out.println("El key nombre existe? " +persona2.containsKey("Nombre")); 
         
          System.out.println("El valor Dario existe? " +persona2.containsValue("Dario2"));
        
        //Limpiando todo el diccionario
        
        persona2.clear();
        
        System.out.println("Nuevo dict despues de limpiarlo: " +persona2);
        
       
        
        
        
        
    }
}
