
package Clase03;
public class Casa extends Lote {
    
    private String direccion;
    
    public Casa(double ancho, double largo, String propietario, String direccion){
    
        super(ancho,largo,propietario); 
        this.direccion = direccion;
    }

    /**
     * @return the direccion
     */
    public String getDireccion() {
        return direccion;
    }

    /**
     * @param direccion the direccion to set
     */
    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    
    
}
