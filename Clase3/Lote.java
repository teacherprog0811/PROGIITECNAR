/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs:/;/nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clase3;

/**
 *
 * @author Ing. Narvaez Mejia
 */
public class Lote {
    
    private double ancho;
    private double largo;
    private String propietario;
    
    
    public Lote(double ancho, double largo, String propietario){
        this.ancho = ancho;
        this.largo = largo;
        this.propietario = propietario;
    
    }

    /**
     * @return the ancho
     */
    public double getAncho() {
        return ancho;
    }

    /**
     * @param ancho the ancho to set
     */
    public void setAncho(double ancho) {
        this.ancho = ancho;
    }

    /**
     * @return the largo
     */
    public double getLargo() {
        return largo;
    }

    /**
     * @param largo the largo to set
     */
    public void setLargo(double largo) {
        this.largo = largo;
    }

    /**
     * @return the propietario
     */
    public String getPropietario() {
        return propietario;
    }

    /**
     * @param propietario the propietario to set
     */
    public void setPropietario(String propietario) {
        this.propietario = propietario;
    }
    
    
}
