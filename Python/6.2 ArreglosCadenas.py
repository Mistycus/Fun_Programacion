print("-------------Arreglo de cadenas------------ ")
mensaje ="Fundamentos de Programacion"
print (mensaje)
print(mensaje[3])
print(mensaje[10])
print(mensaje[11])

# inmutabilidad
notas = [14,20,8,15]
notas[2]=12
print(notas)

palabra = "UPN."
# palabra[3] = "♠"
print(palabra)

texto = palabra[0]+palabra[1]+ palabra[2]+ "♠"
print(texto)

print("concatenacion")
nombre = "Elvis"
apellido = "Jambo"
completo = nombre + " "+ apellido
print(completo)

# longitud de la cadena

cantidad =len(mensaje)
print(f'El Texto{mensaje} tiene una longitud de {cantidad} lentras')
# ultimo caracter
print(f'El Ultimo caracter del texto {mensaje} es {mensaje[len(mensaje) -1]}')

print("-----------RECORRIENDO UNA CADENA---------------")
for i in range(len(mensaje)):
    print(f'{i} -> {mensaje[i]}')

# Ejercicio 
"""
leer un codigo de estudiante y su carrera 
formar una etiqueta 
moestrar la longitud codigo ,carrera, etiqueta
mostrar primer y ultimo caracter del codigo
recorrer cada letra de la carrera
crear una etiqueta agregando el cemestre  sin alterar la original

"""

print ("-----------> INGRESANDO DATOS <------------")
print(" ")
codigo= input ("Ingrese su codigo : ")
carrera = input ("Ingrese su Carrera : ")

etiqueta = codigo + "|" + carrera
etiqueta_periodo = etiqueta + "| 2026 - 2"

print (etiqueta)
print(f'Longitud del codigo  : {len(codigo)}')
print(f'Longitud de la carrera : {len(carrera)}')
print(f'Longitud de la etiqueta :{len(etiqueta)}')
if len(codigo) > 0 :
    print(f' Primer caracter : {codigo[0]}')
    print(f'Ultimo Caracter : {codigo[len(codigo) -1]}')  

print ("Recorriendo la carrera ")
for i in range(len(carrera)):
    print(f'{i} -> {carrera[i]}')

print(etiqueta_periodo)  


