# Importa el paquete sqlite3
import sqlite3

# Crea la base de datos
conn = sqlite3.connect('../database/hotel.db')
cursor = conn.cursor()

# Insertar datos del usuario ROOT
insert_habitacion = """INSERT INTO HABITACION VALUES
('1', '1', 'Mediano', '3 Personas', '35000', 'Libre', ''),
('2', '2', 'Chico', '1 Persona', '20000', 'Requiere Mantenimiento', ''),
('3', '3', 'Grande', '5 Personas','50000', 'Ocupado', '1');"""

insert_reserva = """INSERT INTO RESERVA VALUES
               ('1', '2026-09-01', '2026-09-09', '2026-10-09', 'Activo', '1', '1');"""

insert_factura = """INSERT INTO FACTURA VALUES
('1', '2026-10-09', '50000', '', '50000', '', '1')"""

insert_cliente = """INSERT INTO CLIENTE VALUES
('1', 'Juan Doe', '1234567', '4637041234', 'Juan@Doe')"""

# Mostrar Datos insertadors
cursor.execute(insert_habitacion)
cursor.execute(insert_reserva)
cursor.execute(insert_factura)
cursor.execute(insert_cliente)
print("Se han insertado los datos requeridos ")
cursor.execute("SELECT * FROM HABITACION")
cursor.execute("SELECT * FROM RESERVA")
cursor.execute("SELECT * FROM FACTURA")
cursor.execute("SELECT * FROM CLIENTE")

# Commit changes and close connection
conn.commit()
conn.close()
