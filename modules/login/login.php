<?php
session_start();
$db = new SQLite3('../../database/hotel.db');

if (!$db) {
    die("Problems with connection of the database");
}


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nombre_usuario = $_POST['nombre_usuario'];
    $contrasena = md5($_POST['contrasena']);

    $sql = "SELECT * FROM USUARIO WHERE nombre_usuario = :usuario AND contrasena = :clave";
    $stmt = $db->prepare($sql);
    
    $stmt->bindValue(':usuario', $nombre_usuario, SQLITE3_TEXT);
    $stmt->bindValue(':clave', $contrasena, SQLITE3_TEXT);
    
    $result = $stmt->execute();
	$user_row = $result->fetchArray(SQLITE3_ASSOC);

    if ($user_row) {

        $_SESSION['logged-in'] = true;
        
        foreach ($nombre_usuario as $key => $valor) {
            if ($key !== 'contrasena') {
                $_SESSION[$key] = $valor;
            }
        }
        
        header("Location: ../../index.php");
        exit();
        
    } else {
        echo "<p>Usuario o contraseña incorrectos</p>";
    }
}
?>


<!DOCTYPE html>
<html>
<head>
    <title>Login de Usuarios</title>
	<link rel="stylesheet" type='text/css' href='../style.css'>
	<meta charset='utf-8'/>
	
		
</head>
<body>

<div class="title" align="center">
		  <h1>Iniciar Sesion</h1>
</div>


<div class="main" align="center">
    <form method="POST">
        <p>Ingrese su nombre:</p>
    <input type="text" name="nombre_usuario" required><br>
        <p>Ingrese su contraseña:</p>
    <input type="password" name="contrasena" required><br><br>
        <input type="submit" value="Ingresar">
    </form>
</div> 

<footer>
<div class="footer" align="center">
<h5>¿Aun no tiene una cuenta? <a href="register.php">Crear Cuenta.</a></h5>
<h5>Cambiar contraseña (requiere estar con sesion iniciada) <a href="cambio.php">Cambiar contraseña.</a></h5>
</div>
</footer>

</body>
</html>
