# Importa el paquete sqlite3
import sqlite3

# Crea la base de datos
conn = sqlite3.connect('../database/hotel.db')
cursor = conn.cursor()

# Elimina las tablas si ya existen
cursor.execute("DROP TABLE IF EXISTS USUARIO")
cursor.execute("DROP TABLE IF EXISTS ROL")
cursor.execute("DROP TABLE IF EXISTS RESERVA")
cursor.execute("DROP TABLE IF EXISTS HABITACION")
cursor.execute("DROP TABLE IF EXISTS CLIENTE")
cursor.execute("DROP TABLE IF EXISTS FACTURA")
cursor.execute("DROP TABLE IF EXISTS SERVICIO")

# Creacion de tabla usuario
creacion_tabla_usuario = """
    CREATE TABLE USUARIO (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,              
        nombre_usuario VARCHAR(50) NOT NULL,
        contrasena VARCHAR(255) NOT NULL,
        email VARCHAR(25) NOT NULL,
        estado VARCHAR(45),
        rol_idrol INT
    );
"""

# Creacion tabla Rol
creacion_tabla_rol = """
    CREATE TABLE ROL (
        id_rol INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_rol VARCHAR(25) NOT NULL,
        descripcion VARCHAR(45)
    );
"""

# Creacion tabla Reserva
creacion_tabla_reserva = """
    CREATE TABLE RESERVA (
        id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,     
        fecha_reserva DATE,
        fecha_ingreso DATE,
        fecha_salida DATE,
        estado_reserva TEXT NOT NULL CHECK (estado_reserva IN ('Activo', 'Inactivo', 'Pendiente')),
        cliente_id_cliente INT
    );
"""

# Creacion tabla Habitacion
creacion_tabla_habitacion = """
    CREATE TABLE HABITACION (
        id_habitacion INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INT,
        tipo VARCHAR(45),
        capacidad VARCHAR(45),
        precio_noche DECIMAL(10,2),
        estado_habitacion TEXT NOT NULL CHECK (estado_habitacion IN ('Libre', 'Ocupado', 'Requiere Mantenimiento')),
        reserva_id_reserva INT
    );
"""

# Creacion tabla Cliente
creacion_tabla_cliente = """
    CREATE TABLE CLIENTE (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_apellido VARCHAR(255) NOT NULL,
        dni VARCHAR(10) NOT NULL,
        telefono VARCHAR(45),
        correo VARCHAR(45),
        direccion VARCHAR(45)
    );
"""

# Creacion tabla Factura
creacion_tabla_factura = """
    CREATE TABLE FACTURA (
        id_factura INTEGER PRIMARY KEY AUTOINCREMENT, 
        fecha_emision DATE,
        subtotal_hospedaje DECIMAL(10,2),
        subtotal_servicios DECIMAL(10,2),
        total DECIMAL(10,2),
        reserva_id_reserva INT
    );
"""


# Creacion tabla Servicio
creacion_tabla_servicio = """
    CREATE TABLE SERVICIO (
        id_servicio INTEGER PRIMARY KEY AUTOINCREMENT,  
        nombre_servicio VARCHAR(255) NOT NULL,
        descripcion VARCHAR(255) NOT NULL,
        precio_unitario DECIMAL(10,2),
        factura_id_factura INT
    );
"""

# Insert en la tabla Usuario

insert_tabla_usuario = """
    INSERT INTO USUARIO
VALUES ('1', 'admin', 'admin', 'admin@admin', 'activo', 1);
"""

# Insert en la tabla Rol
insert_tabla_rol = """
    INSERT INTO ROL (id_rol, nombre_rol, descripcion) VALUES
(1, 'admin', 'permisos de administrador'),
(2, 'usuario', 'permisos de usuario comun');
"""

# Execute the table creation query
cursor.execute(creacion_tabla_usuario)
print("La tabla Usuario esta lista")
cursor.execute(creacion_tabla_rol)
print("La tabla Rol esta lista")
cursor.execute(creacion_tabla_reserva)
print("La tabla Reserva esta lista")
cursor.execute(creacion_tabla_cliente)
print("La tabla Cliente esta lista")
cursor.execute(creacion_tabla_factura)
print("La tabla Factura esta lista")
cursor.execute(creacion_tabla_servicio)
print("La tabla Servicio esta lista")
cursor.execute(creacion_tabla_habitacion)
print("La tabla Habitacion esta lista")
cursor.execute(insert_tabla_usuario)
print("La tabla Usuario ahora esta cargada")
cursor.execute(insert_tabla_rol)
print("La tabla Rol ahora esta cargada")

# Confirm that the table has been created
print("Las tablas estan listas")

# Close the connection to the database
conn.close()
