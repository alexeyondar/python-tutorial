import sqlite3
from datetime import datetime

# Abro la base de datos si existe o la creo
connection = sqlite3.connect("B:\\Developer\\Phyton\\Tutorial\\test.db")

# Voy a crear tablas, para eso uso el método cursor de la conexion, este nos
# permite ejecutar
# sentencias sql en la base de datos
cursor = connection.cursor()
cursor.execute("DROP TABLE Personas")
cursor.execute("CREATE TABLE Personas (Nombres TEXT, Apellidos TEXT, FechaNacimiento DATE)")

fechaNacimiento = datetime(1981,8,6)

# Insertaré datos a la tabla Personas
cursor.execute("INSERT INTO Personas VALUES('Mauricio', 'Montoya Medrano', '{}')".format(fechaNacimiento.strftime("%d/%m/%Y")))

# Insertaré varios registros
personas = [
    ("Lissete Katiana", "González Ochoa", datetime(1986,9,5).strftime("%d/%m/%Y")),
    ("Clara Eugenia", "Castrillón Medrano", datetime(1992,5,29).strftime("%d/%m/%Y")),
    ("Diana Marcela", "González Ochoa", datetime(1982,4,14).strftime("%d/%m/%Y"))
]

cursor.executemany("INSERT INTO Personas VALUES(?,?,?)", personas)
connection.commit()

# Selecciono todos los registros de la base de datos
cursor.execute("SELECT * FROM Personas")
response = cursor.fetchall()
for persona in response:
    print(persona)

connection.close()
