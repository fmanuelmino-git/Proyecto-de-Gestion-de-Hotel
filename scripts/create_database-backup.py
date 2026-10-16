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
cursor.execute("DROP TABLE IF EXISTS ESTADIA")
cursor.execute("DROP TABLE IF EXISTS CONSUMO")
cursor.execute("DROP TABLE IF EXISTS SERVICIO")

# Creacion de tabla usuario
creacion_tabla_usuario = """
    CREATE TABLE USUARIO (
        id_usuario INT PRIMARY KEY,              
        nombre_usuario VARCHAR(255) NOT NULL,
        contrasena VARCHAR(25) NOT NULL,
        email VARCHAR(25) NOT NULL,
        estado VARCHAR(45),
        rol_idrol INT
    );
"""

# Creacion tabla Rol
creacion_tabla_rol = """
    CREATE TABLE ROL (
        id_rol INT PRIMARY KEY,              
        nombre_rol VARCHAR(255) NOT NULL,
        descripcion VARCHAR(45),
        usuario_id_usuario INT
    );
"""

# Creacion tabla Reserva
creacion_tabla_reserva = """
    CREATE TABLE RESERVA (
        id_reserva INT PRIMARY KEY,              
        fecha_reserva DATE,
        fecha_ingreso DATE,
        fecha_salida DATE,
        estado_reserva TEXT NOT NULL CHECK (estado_reserva IN ('activo', 'inactivo', 'pendiente')),
        factura_id_factura INT
    );
"""

# Creacion tabla Habitacion
creacion_tabla_habitacion = """
    CREATE TABLE HABITACION (
        id_habitacion INT PRIMARY KEY,              
        numero INT,
        tipo VARCHAR(45),
        capacidad VARCHAR(45),
        precio_noche DECIMAL(10,2),
        estado_habitacion TEXT NOT NULL CHECK (estado_habitacion IN ('libre', 'ocupado', 'requiere mantenimiento')),
        red_id_reserva INT
    );
"""

# Creacion tabla Cliente
creacion_tabla_cliente = """
    CREATE TABLE CLIENTE (
        id_cliente INT PRIMARY KEY,              
        nombre_apellido VARCHAR(255) NOT NULL,
        dni VARCHAR(10) NOT NULL,
        telefono VARCHAR(45),
        correo VARCHAR(45)
    );
"""

# Creacion tabla Factura
creacion_tabla_factura = """
    CREATE TABLE FACTURA (
        id_factura INT PRIMARY KEY,              
        fecha_emision DATE,
        subtotal_hospedaje DECIMAL(10,2),
        subtotal_servicios DECIMAL(10,2),
        total DECIMAL(10,2),
        servicio_id_servicio INT,
        cliente_id_cliente INT
    );
"""


# Creacion tabla Servicio
creacion_tabla_servicio = """
    CREATE TABLE SERVICIO (
        id_servicio INT PRIMARY KEY,              
        nombre_servicio VARCHAR(255) NOT NULL,
        descripcion VARCHAR(255) NOT NULL,
        precio_unitario DECIMAL(10,2)
    );
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

# Confirm that the table has been created
print("Las tablas estan listas")

# Close the connection to the database
conn.close()
