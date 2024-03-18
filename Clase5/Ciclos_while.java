
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

/**
 *
 * @author Ing. Narvaez Mejia
 */
public class Ciclos_while {

    public static void main(String[] args) {
        
        boolean ciclo = true;
        while(ciclo){
        Scanner lectura = new Scanner (System.in);
        System.out.println("MENU PRINCIPAL: \n 1. PERSONAS.\n 2. VEHICULOS.\n 3. UNIVERSIDADES.\n 4. NOTAS.\n 5. SALIR");
        System.out.println("DIGITA UNA OPCION: ");
        int opcion = lectura.nextInt();
        
        switch(opcion){
        
            case 1: 
                System.out.println("SELECCIONASTE LA OPCION PERSONAS");
                ciclo =true;
                break;
            case 2:
                System.out.println("SELECCIONASTE LA OPCION VEHICULOS");
                ciclo =true;
                break;
            case 3:
                System.out.println("SELECCIONASTE LA OPCION UNIVERSIDADES");
                ciclo =true;
                break;
            case 4:
                System.out.println("SELECCIONASTE LA OPCION NOTAS");
                ciclo =true;
                break;
            case 5: 
                System.out.println("HASTA LUEGO");
                ciclo =false;
                break;
            default:
                System.out.println("HAS DIGITADO UNA OPCION INVALIDA");
                break;
               
        }
        
        }
    }
}
