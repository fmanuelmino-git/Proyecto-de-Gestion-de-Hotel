# Importa el paquete sqlite3
import sqlite3

# Crea la base de datos
conn = sqlite3.connect('../database/hotel.db')
cursor = conn.cursor()

# Insertar datos del usuario ROOT
cursor.execute("INSERT INTO HABITACION (id_habitacion, numero, tipo, capacidad, precio_noche, estado_habitacion, reserva_id_reserva) VALUES
('1', '1', 'Mediano', '3 Personas', '35000', 'Libre', ''),
('2', '2', 'Pequeño', '1 Persona', '20000', 'Requiere Mantenimiento', ''),
('3', '3', 'Grande', '5 Personas','50000', 'Ocupado', '1');")

cursor.execute("INSERT INTO RESERVA (id_reserva, fecha_reserva, fecha_ingreso, fecha_salida, estado_reserva, factura_id_factura, cliente_id_cliente) VALUES
('1', '2026-09-01', '2026-09-09', '2026-10-09' 'Activo', '1', '1');")

cursor.execute("INSERT INTO FACTURA (id_factura, fecha_emision, subtotal_hospedaje, subtotal_servicios, total, servicio_id_servicio, reserva_id_reserva) VALUES
('1', '2026-10-09', '50000', '', '1')")

cursor.execute("INSERT INTO CLIENTE (id_cliente, nombre_apellido, dni, telefono, correo) VALUES ('1', 'Juan Doe', '1234567', '4637041234', 'Juan@Doe')")

# Mostrar Datos insertadors
print("Se han insertado los datos requeridos ")
cursor.execute("SELECT * FROM HABITACION")
cursor.execute("SELECT * FROM RESERVA")
cursor.execute("SELECT * FROM FACTURA")
cursor.execute("SELECT * FROM CLIENTE")

# Commit changes and close connection
conn.commit()
conn.close()
