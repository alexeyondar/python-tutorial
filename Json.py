import json

# Convertimos un diccionario Python a una estructura JSON
producto1 = { "Nombre": "Silla", "Color": "Rojo", "Precio": 650000 }
js = json.dumps(producto1)
print(js)

# Como producto1 es un diccionario, se puede acceder a el contenido de este
# como si fuera un array
print(producto1["Nombre"])

# Convertimos un JSON a un diccionario de Python
producto2 = json.loads(js)
print(producto2)
