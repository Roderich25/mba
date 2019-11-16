<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Confirmación</title>
</head>
<body>

<p>El alumno con nombre ${elAlumno.getNombre()}, apellido ${elAlumno.getApellido()} y edad ${elAlumno.getEdad()} se ha registrado con éxito.</p>
<p>La asignatra elegida es ${elAlumno.getOptativa()}.</p>
<p>La ciudad de estudios será ${elAlumno.getCiudad()}.</p>
<p>El idiomas será ${elAlumno.getIdioma()}.</p>
<p>Información enviada a ${elAlumno.getEmail()} </p>
<p>Código Postal: ${elAlumo.getCodigoPostal()}</p>
</body>
</html>