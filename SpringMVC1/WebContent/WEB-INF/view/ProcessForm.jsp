<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/resources/css/base.css">
<title>Insert title here</title>
</head>
<body>
<h1 style="text-align:center">Welcome ${param.name}, to the Spring World!</h1>

<h3> ${message} </h3>

<img alt="leaf" src="${pageContext.request.contextPath}/resources/images/spring.png">

</body>
</html>