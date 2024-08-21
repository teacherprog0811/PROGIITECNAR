
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

/**
 *
 * @author Ing. Narvaez Mejia
 */
public class EjercicioMenu {

    public static void main(String[] args) {
        
        Scanner lectura = new Scanner (System.in);
        System.out.println("MENU PRINCIPAL: \n 1. PERSONAS.\n 2. VEHICULOS.\n 3. UNIVERSIDADES.\n 4. NOTAS.\n 5. SALIR");
        System.out.println("DIGITA UNA OPCION: ");
        int opcion = lectura.nextInt();
        
        switch(opcion){
        
            case 1: 
                System.out.println("SELECCIONASTE LA OPCION PERSONAS");
                break;
            case 2:
                System.out.println("SELECCIONASTE LA OPCION VEHICULOS");
                break;
            case 3:
                System.out.println("SELECCIONASTE LA OPCION UNIVERSIDADES");
                
                break;
            case 4:
                System.out.println("SELECCIONASTE LA OPCION NOTAS");
                break;
            case 5: 
                System.out.println("HASTA LUEGO");
                break;
            default:
                System.out.println("HAS DIGITADO UNA OPCION INVALIDA");
                break;
               
        }
        
     
    }
}
