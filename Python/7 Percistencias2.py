print("  ")
print("------operaciones abrir , leer , escribir y cerrar archivos-------")
#utilizar iport os

import os
nombre_archivo ="python\\escribir.txt"
#obtener la ruta 
ruta_completa =os.path.abspath(nombre_archivo)
print(f'Nombre archivo : {nombre_archivo}')
print(f'ruta completa : {ruta_completa}')

#escibir 
archivo= open(nombre_archivo,"w" , encoding="utf-8")
archivo.write("archivo abrierto en modo escritura . \n")
archivo.close()

print("archivo creado y escrito correctamente ")

# escrivir varias lineas

with open (nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Maria \n")
    archivo.write("Esperanza \n")
    archivo.write("Sofia \n")


print("datos escritos correctamente")

#escribir sin eliminar 
with open (nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("Maria Fernanda \n")
    archivo.write("Elvis \n")
    archivo.write("Edith \n")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido= archivo.read()

print(contenido)

# leer linea por linea
with open (nombre_archivo, "r",  encoding="utf-8") as archivo:
    linea1=archivo.readline()
    linea2=archivo.readline()
    linea3=archivo.readline()
    linea4=archivo.readline()
    linea5=archivo.readline()

print (f'linea 1 :{linea1}')
print (f'linea 2 :{linea2}')
print (f'linea 3 :{linea3}')
print (f'linea 4 :{linea4}')
print (f'linea 5 :{linea5}')

# leer como seleccion 

with open (nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido =archivo.readlines()
for i in range(len(contenido)):
    print(f'linea {i+1}: {contenido[i].strip()}')
