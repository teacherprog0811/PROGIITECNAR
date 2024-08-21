 package Clase6;

 import java.util.ArrayList;
 import java.util.Collections;
 

 public class EjercicioVectores {
 
     public static void main(String[] args) {
         
         ArrayList<Integer> arrList = new ArrayList<Integer>();  
         arrList.add(0, 100);
         arrList.add(1, 300);
         arrList.add(2, 400);
         arrList.add(3, 700);
         arrList.add(4, 500);
         arrList.add(5, 600);
   
         System.out.println("Imprimiendo Lista" +arrList);
         
         arrList.remove(1);
         System.out.println("Imprimiendo Lista despues de eliminacion" +arrList);
         
         arrList.clear();
         System.out.println("Imprimiendo Lista despues de vaciada" +arrList);
         System.out.println("Imprimiendo primer elemento" +arrList.getFirst());
         System.out.println("Imprimiendo ultimo elemento" +arrList.getLast());
         System.out.println("El tamaño de la lista es: " +arrList.size());
         System.out.println("El valor 1 esta en la lista ? " +arrList.contains(1));
         
         System.out.println("Invirtiendo la lista:  " +arrList.reversed());
         Collections.sort(arrList);
         System.out.println("Ordenando la lista:  " +arrList);
     }
 }
 