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
with open("python\estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("susana\nDiana\nMaria\n")

with open("python\estudiantes.txt", "r", encoding="utf-8") as archivo:
    posicion_inicial = archivo.tell()
    primera_linea = archivo.readline()
    posicion_final = archivo.tell()

print(f'Posicion inicial :{posicion_inicial}')
print(f'Primera linea :{primera_linea}')
print(f'Posicion final  :{posicion_final}')

print ("operaciones con punteros ")