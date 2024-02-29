/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

 //package com.mycompany.personas;

 /**
  *
  * @author Ing. Narvaez Mejia
  */
 public class Personas {
 
     public static void main(String[] args) {
         
         Persona p = new Persona();
         p.setNombre("Ivan Narvaez");
         p.setSalario(10000);
         p.setGastos(2000);
         //p.Devengado(p.getSalario(), p.getGastos());
         System.out.println(p.getNombre());
         System.out.print(p.Devengado(p.getSalario(), p.getGastos()));
     }
 }
 