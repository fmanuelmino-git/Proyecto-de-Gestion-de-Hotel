# Importa el paquete sqlite3
import sqlite3

# Crea la base de datos
conn = sqlite3.connect('../database/hotel.db')
cursor = conn.cursor()

# Insert en la tabla Usuario

insert_tabla_usuario = """
    INSERT INTO USUARIO
VALUES ('1', 'admin', 'admin', 'admin@admin', 'activo', '1', '1');
"""

# Insert en la tabla Rol
insert_tabla_rol = """
    INSERT INTO ROL (id_rol, nombre_rol, descripcion) VALUES
(1, 'admin', 'permisos de administrador'),
(2, 'usuario', 'permisos de usuario comun');
"""
# Insertar datos del usuario ROOT
insert_root = """ INSERT INTO USUARIO VALUES ('1', 'root', 'root', 'root@root', '1');"""

insert_habitacion = """INSERT INTO HABITACION VALUES
('1', '1', 'Mediano', '3 Personas', '35000', 'Libre', ''),
('2', '2', 'Chico', '1 Persona', '20000', 'Requiere Mantenimiento', ''),
('3', '3', 'Grande', '5 Personas','50000', 'Ocupado', '1');"""

insert_reserva = """INSERT INTO RESERVA VALUES
               ('1', '2026-09-01', '2026-09-09', '2026-10-09', 'Activo', '1');"""

insert_factura = """INSERT INTO FACTURA VALUES
('1', '2026-10-09', '50000', '', '50000', '1')"""

insert_cliente = """INSERT INTO CLIENTE VALUES
('1', 'Juan Doe', '1234567', '4637041234', 'Juan@Doe', '')"""

# Mostrar Datos insertadors
cursor.execute(insert_tabla_usuario)
cursor.execute(insert_tabla_rol)
cursor.execute(insert_habitacion)
cursor.execute(insert_reserva)
cursor.execute(insert_factura)
cursor.execute(insert_cliente)
print("Se han insertado los datos requeridos ")

# Commit changes and close connection
conn.commit()
conn.close()
