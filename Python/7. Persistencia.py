print("percistenciad e datos")
# capacidad de concervar  iformacion despues d eterminar una ejecucion 
# crear archivo . txt , escribir un mensaje 
with open("python\datos.txt" , "w" , encoding="utf-8") as archivo:
    archivo.write("hola Estudiantes\n")

print("Archivo creado correctamente ")

# abrir el archivo leer el contenido 
with open("python\datos.txt", "r" , encoding="utf-8") as archivo:
    contenido = archivo.read();

print(f'Contenido : {contenido}')

print ("puntero de un archivo ")
# crear un archivo ..  apuntar a undice 
with open("python\\estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("susana\nDiana\nMaria\n")

with open("python\\estudiantes.txt", "r", encoding="utf-8") as archivo:
    posicion_inicial = archivo.tell()
    primera_linea = archivo.readline()
    posicion_final = archivo.tell()

print(f'Posicion inicial :{posicion_inicial}')
print(f'Primera linea :{primera_linea}')
print(f'Posicion final  :{posicion_final}')

print ("operaciones con punteros ")


with open("python\\condigo.txt", "w" , encoding ="utf-8") as archivo:
    archivo.write("UPN2026")

with open("python\condigo.txt", "r" , encoding ="utf-8") as archivo:
    #puntero se mueve a la posicion 2 
    archivo.seek(2)
    posicion_actual = archivo.tell()
    contenido = archivo.read()

print (f'posicion actual : {posicion_actual}')
print (f'contenido leido :{contenido}')

print("archivos de texto con datos legibles")

with open ("python\\notas.txt","w", encoding="utf-8") as archivo:
    archivo.write("estudiante:susana\n")
    archivo.write("notas :17\n")
    archivo.write("estado : aprobado\n")

with open("python\\notas.txt","r", encoding="utf-8") as archivo:
    contenido=archivo.read()

print(contenido)

print("  ")
print("------Archivo Binario-------")
# Almacenar Bytes
with open("python\\numero.bin ", "wb") as archivo:
    archivo.write(bytes([64,65,66,67,68,69,70]))

with open ("python\\numero.bin" , "rb") as archivo:
    datos =archivo.read()

print(f'datos binarios : {datos}')

