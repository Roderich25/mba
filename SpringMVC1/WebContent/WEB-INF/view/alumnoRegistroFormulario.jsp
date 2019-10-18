<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title></title>
</head>
<body>
	<form:form action="procesarFormulario" modelAttribute="elAlumno" method="post">
		
		Nombre: <form:input path="nombre"/>
		<form:errors path="nombre" style="color:red"/><br>
		
		Apellido: <form:input path="apellido"/><br>
		
		E-mail: <form:input path="email"/>
		<form:errors path="email" style="color:red"/><br>
		
		Edad: <form:input path="edad" type="number"/>
		<form:errors path="edad" style="color:red"/><br>		
		
		Asignatura Optativa:
		<form:select path="optativa" multiple="true">
			<form:option value="mathematics" label="Matematicas"/>
			<form:option value="statistics" label="Estadística"/>
			<form:option value="probability" label="Probabilidad"/>
			<form:option value="machine learning" label="Aprendizaje de Máquina"/>
			<form:option value="deep learning" label="Deep Learning"/>
		</form:select>
		<br>
		Barcelona<form:radiobutton path="ciudad" value="Barcelona"/><br>
		Madrid<form:radiobutton path="ciudad" value="Madrid"/><br>
		Valencia<form:radiobutton path="ciudad" value="Valencia"/><br>	
		<br>
		English<form:checkbox path="idioma" value="Ingles"/><br>
		Français<form:checkbox path="idioma" value="Frances"/><br>
		Español<form:checkbox path="idioma" value="Español"/><br>
		<br>
		<input type="submit" value="Enviar"/>
	</form:form>
</body>
</html>