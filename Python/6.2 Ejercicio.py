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