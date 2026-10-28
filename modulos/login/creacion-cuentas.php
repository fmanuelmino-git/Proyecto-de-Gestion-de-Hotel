<?php

session_start();
$db = new SQLite3('../../database/hotel.db');

if (!$db) {
    die("Problems with connection of the database");
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nombre_usuario = $_POST['nombre_usuario'];
	$email = $_POST['email'];
    $contrasena = $_POST['contrasena'];
	$nombre_apellido = $_POST['nombre_apellido'];
	$dni = $_POST['dni'];
	$telefono = $_POST['telefono'];

    $sql = "INSERT INTO USUARIO (nombre_usuario, email, contrasena, estado) 
            VALUES ('$nombre_usuario', '$email', '$contrasena', 'activo');
			INSERT INTO PERSONA (nombre_apellido, dni, telefono) 
			VALUES ('$nombre_apellido', '$dni', '$telefono');";

    $result = $db->exec($sql);
    if ($result) {
        echo "Usuario registrado correctamente. <a href='login.php'>Ir al login</a>";
    } else {
        // 3. Así se muestran los errores en SQLite3
        echo "Error: " . $db->lastErrorMsg();
    }
}
?>

<!DOCTYPE html>
<html lang='es'>

	<head>

		<title>Proyecto de Gestion de Hotel</title>
		<link rel="stylesheet" type='text/css' href='../style.css'>
		<meta charset='utf-8'/>
</head>
<body>
<main>
<div class="title" align="center">
<h1>Crear Cuenta</h1>
</div>

<div class="main" align="center">
  <form method="post">
    <p>Ingrese su nombre de usuario:</p>
    <input type="text" name="nombre_usuario" required>
    <br>
	<p>Ingrese su nombre real completo:</p>
	<input type="text" name="nombre_apellido" required>
	<br>
    <p>Ingrese su Email:</p>
	<input type="text" name="email" required>
	<br>
	<p>Ingrese su DNI:</p>
	<input type="text" name="dni" required>
	<br>
	<p>Ingrese su numero telefonico:</p>
	<input type="text" name="telefono" required>
	<br>
	<p>Ingrese su Contraseña:</p>
	<input type="password" name="contrasena" required>
	<br>
     <button type="submit">Registrarse</button>
  </form>
 </div>
 
</main>
</body>
</html>
