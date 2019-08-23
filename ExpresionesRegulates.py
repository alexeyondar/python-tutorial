import re

text = "Hola, mi nombre es Mauricio y mi correo es mcubico33@gmail.com"

# Busco la palabra en el texto, si encuentra algo, retorna un objeto de tipo re.Match
# sino, retorna null
response:re.Match = re.search("Mauricio", text)

if(response):
    print("Texto encontrado")
    print(response)
else:
    print("Texto NO encontrado")

# Verifico si el texto termina con la palabra com
response = re.search("com$", text)
if(response):
    print("Texto encontrado")
    print(response)
else:
    print("Texto NO encontrado")

response = re.search("gmail$", text)
if(response):
    print("Texto encontrado")
    print(response)
else:
    print("Texto NO encontrado")

# Verifico si el texto empieza con la palabra Hola
response = re.search("^Hola", text)
if(response):
    print("Texto encontrado")
    print(response)
else:
    print("Texto NO encontrado")

# Verifico que exista en el texto la palabra 'mi' y 'es' y entre las dos existen otros caracteres
response = re.search("mi.*es", text)
response = re.search("^Hola", text)
if(response):
    print("Texto encontrado")
    print(response)
else:
    print("Texto NO encontrado")

text = """
Mi auto es rojo,
el auto de a lenin es gris
y el auto de pedro es rojo con plata
"""

# Busco en todo el texto la palabra 'coche' y que termine con la palabra 'rojo'
response = re.findall("auto.*rojo", text)
if(response):
    print("Texto encontrado")
    print(response)
else:
    print("Texto NO encontrado")