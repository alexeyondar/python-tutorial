import os
import pickle

filename = "B:\\Developer\\Phyton\\Tutorial\\Fichero.txt"
filenameAux = "B:\\Developer\\Phyton\\Tutorial\\FicheroAux.txt"

# Abro el fichero en modo escritura (r) de texto (t)
file = open(filename, "r")

# Obtengo todas las líneas del fichero
lineas = file.read()
print(lineas)

# Creo un nuevo fichero si no existe y limpio su contenido
file = open(filenameAux,"w")
text = "Línea 1"

# Escribo en el fichero auxiliar
file.write(text)
file.close()

file = open(filenameAux, "r")
lineas = file.read()
print(lineas)

# Escribo una segunda línea en el fichero auxiliar
file = open(filenameAux, "a")
text = "\nLínea 2"
file.write(text)
file.close()

file = open(filenameAux, "r")
lineas = file.read()
print(lineas)
file.close()

# Elimino el fichero auxiliar
if(file.closed):
    os.remove(filenameAux)

#-------------------------- FICHEROS EN FORMATO BINARIO O SERIALIZADOS
filenameBinario = "FicheroBinario.pickle"
file = open(filenameBinario, "wb")
list = ["Verde", "Blanco", "Negro", "Rojo", "Azul"]

# Serializo el objeto list y lo imprimo en el archivo binario
pickle.dump(list, file)
file.close()

# Deserializo el objeto pickle
file = open(filenameBinario, "rb")
list = pickle.load(file)
file.close()
print(list)

if(file.closed):
    os.remove(filenameBinario)