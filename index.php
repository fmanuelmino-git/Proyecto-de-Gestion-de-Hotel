<?php
session_start();
$db = new SQLite3('database/hotel.db');

if (!$db) {
    die("Problems with connection of the database");
}
?>

<!DOCTYPE html>
<html lang='es'>

<head>
	<title>Proyecto de Gestion de Hotel</title>
	<link rel="stylesheet" type='text/css' href='style.css'>
	<meta charset='utf-8'/>		
</head>

<body>

<div class="sidenav">
	<a href="modulos/proyectos/listbyprojects.php">Lista de Habitaciones</a>
	<a href="modulos/reportes/reporte.php">Reportes</a>
	<a href="modulos/busqueda/busqueda.php">Busqueda</a>
	<a href="modulos/login/login.php">Iniciar Sesion</a>
	<?php if (isset($_SESSION['logged-in']) && $_SESSION['logged-in'] === true): ?>
	<a href="modules/proyectos/listbyuser.php">Proyectos Propios</a>
	<a href="modules/login/logout.php">Cerrar sesion</a>
	<?php endif; ?>
</div> 

<div class="title">
	<h2> Proyecto de Gestion de Hotel</h2>
</div>

<div class="main">
    <?php
      $registros = $db->query("SELECT h.numero, h.tipo, h.capacidad, h.estado_habitacion, r.fecha_salida, c.nombre_apellido FROM HABITACION as h LEFT OUTER JOIN RESERVA as r ON h.reserva_id_reserva = r.id_reserva LEFT OUTER JOIN CLIENTE as c ON r.cliente_id_cliente = c.id_cliente;") or
    die($DB->error);
?>
		<p>.</p>

      <table class="tablalistado">
      <tr><th>Numero de habitacion</th><th>Tipo</th><th>Capacidad</th><th>Estado de habitacion</th><th>Fecha de liberacion</th><th>Inquilino</th></tr>

<?php

        while ($reg = $registros->fetchArray(SQLITE3_ASSOC)) {
        echo '<tr>';
        echo '<td>' . $reg['numero'] . '</td>';
        echo '<td>' . $reg['tipo'] . '</td>';
        echo '<td>' . $reg['capacidad'] . '</td>';
        echo '<td>' . $reg['estado_habitacion'] . '</td>';
		echo '<td>' . $reg['fecha_salida'] . '</td>';
        echo '<td>' . $reg['nombre_apellido'] . '</td>';
        echo '</tr>';

  }
    ?>
    </table>
	<?php if (isset($_SESSION['logged-in']) && $_SESSION['logged-in'] === true): ?>
	<a href="modules/proyectos/listbyuser.php">Insertar nuevas habitaciones</a>
	<p></p>
	<a href="modules/login/logout.php">Modificar habitaciones</a>
	<?php endif; ?>
</div> 
</body>

<footer>
<div class="footer" align="center">
<h5>Proyecto Gestion de Hotel - Demostracion</h5>
</div>
</footer>
  
</html>
