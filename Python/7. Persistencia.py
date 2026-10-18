print("percistenciad e datos")
# crear archivo . txt , escribir un mensaje 
with open("python\datos.txt" , "w" , encoding="utf-8") as archivo:
    archivo.write("hola Estudiantes\n")

print("Archivo creado correctamente ")

# abrir el archivo leer el contenido 
with open("python\datos.txt", "r" , encoding="utf-8") as archivo:
    contenido = archivo.read();

print(f'Contenido : {contenido}')