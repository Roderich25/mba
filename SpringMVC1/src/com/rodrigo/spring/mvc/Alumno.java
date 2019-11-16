package com.rodrigo.spring.mvc;


import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;
import javax.validation.constraints.Email;

public class Alumno {
	
	@NotNull
	@Size(min=2, message="Please fill out the name field.")
	private String nombre;
	
	private String apellido;
	
	@Email
	private String email;
	
	@Pattern(regexp="[0-9]{5}", message="Solo 5 valores númericos!")
	private String codigoPostal;
	
	@Min(value=10, message="Enter a valid age greater than 10 yeard old.")
	@Max(value=100, message="Maximum age is 100 years old.")
	private int edad;
	
	private String optativa;
	
	private String ciudad;
	
	private String idioma;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellido() {
		return apellido;
	}

	public void setApellido(String apellido) {
		this.apellido = apellido;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getCodigoPostal() {
		return codigoPostal;
	}

	public void setCodigoPostal(String codigoPostal) {
		this.codigoPostal = codigoPostal;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public String getOptativa() {
		return optativa;
	}

	public void setOptativa(String optativa) {
		this.optativa = optativa;
	}

	public String getCiudad() {
		return ciudad;
	}

	public void setCiudad(String ciudad) {
		this.ciudad = ciudad;
	}

	public String getIdioma() {
		return idioma;
	}

	public void setIdioma(String idioma) {
		this.idioma = idioma;
	}
	
	

}
