/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
//package com.mycompany.personas;

/**
 *
 * @author Ing. Narvaez Mejia
 */
public class Persona {
    
    private int cedula;
    private String nombre;
    private String apellido;
    private String correo;
    private double salario;
    private double gastos;
    private double tdevengado;
    
    
    
    public double Devengado(double s,double g){
        this.salario = s;
        this.gastos = g;
        this.tdevengado = this.salario - this.gastos;
        
        return (this.tdevengado);
        
    }
    
    /**
     * @return the cedula
     */
    public int getCedula() {
        return cedula;
    }

    /**
     * @param cedula the cedula to set
     */
    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /**
     * @return the apellido
     */
    public String getApellido() {
        return apellido;
    }

    /**
     * @param apellido the apellido to set
     */
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    /**
     * @return the correo
     */
    public String getCorreo() {
        return correo;
    }

    /**
     * @param correo the correo to set
     */
    public void setCorreo(String correo) {
        this.correo = correo;
    }

    /**
     * @return the salario
     */
    public double getSalario() {
        return salario;
    }

    /**
     * @param salario the salario to set
     */
    public void setSalario(double salario) {
        this.salario = salario;
    }

    /**
     * @return the gastos
     */
    public double getGastos() {
        return gastos;
    }

    /**
     * @param gastos the gastos to set
     */
    public void setGastos(double gastos) {
        this.gastos = gastos;
    }

    /**
     * @return the tdevengado
     */
    public double getTdevengado() {
        return tdevengado;
    }

    /**
     * @param tdevengado the tdevengado to set
     */
    public void setTdevengado(double tdevengado) {
        this.tdevengado = tdevengado;
    }
    
    
    
}
