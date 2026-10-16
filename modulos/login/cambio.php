<?php
session_start();
$db = new SQLite3('../../database/hotel.db');

if (!$db) {
    die("Problems with connection of the database");
}

if (!isset($_SESSION['logged-in'])) {
    header("Location: login.php");
    exit;
}

$error = '';
$success = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $current_password = $_POST['current_password'] ?? '';
    $new_password = $_POST['new_password'] ?? '';
    $confirm_password = $_POST['confirm_password'] ?? '';

    if (empty($current_password) || empty($new_password) || empty($confirm_password)) {
        $error = "Todos los campos son obligatorios.";
    } elseif ($new_password !== $confirm_password) {
        $error = "Las nuevas contraseñas no coinciden.";
    } else {
        // 1. Obtener el hash actual almacenado en SQLite
        $stmt = $conn->prepare("SELECT contrasena FROM usuario WHERE id_usuario = :id ;");
        $stmt->execute([':id' => $_SESSION['id_usuario']]);
        $user = $stmt->fetch();

        if ($user) {
            $stored_hash = $user['password'];
            $is_valid = false;

            // 2. Verificar la contraseña actual (Soporte híbrido)
            if (strpos($stored_hash, '$2y$') === 0) {
                // Si ya es un hash seguro moderno (BCRYPT empieza con $2y$)
                $is_valid = password_verify($current_password, $stored_hash);
            } else {
                // Si todavía es un hash MD5 antiguo (comparación directa en minúsculas)
                $is_valid = (strtolower(md5($current_password)) === strtolower($stored_hash));
            }

            // 3. Si la contraseña actual es correcta, procedemos al cambio
            if ($is_valid) {
                // Encriptamos la NUEVA contraseña usando el estándar seguro de PHP
                $new_secure_hash = password_hash($new_password, PASSWORD_DEFAULT);
                
                $update_stmt = $conn->prepare("UPDATE usuario SET contrasena = :password WHERE id_usuario = :id");
                $update_stmt->execute([
                    ':password' => $new_secure_hash,
                    ':id' => $_SESSION['id_usuario']
                ]);

                $success = "¡Contraseña actualizada con éxito al nuevo formato seguro!";
            } else {
                $error = "La contraseña actual es incorrecta.";
            }
        } else {
            $error = "Usuario no encontrado.";
        }
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
        <p>Ingrese su contraseña actual</p>
    <input type="password" id="current_password" name="current_password" required><br>
	<p>Ingrese su contraseña nueva</p>
    <input type="password" id="new_password" name="new_password" required><br>
        <p>Ingrese su contraseña:</p>
    <input type="password" id="confirm_password" name="confirm_password" required><br><br>
        <input type="submit" value="Ingresar">
    </form>
</div> 

<footer>
<div class="footer" align="center">
<h5>¿Desea Volver? <a href="/login.php">Inicio.</a></h5>
</div>
</footer>

</body>
</html>
