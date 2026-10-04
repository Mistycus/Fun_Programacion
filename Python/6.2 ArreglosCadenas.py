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

 

print("---------METODOS TRABAJAR EN CADENAS---------")
# Find

nombre = "Elvis , Jambo"
posicion_coma= nombre.find(",")

print(f' la como esta en la posicion : {posicion_coma}')

# Slicing (extraer subcadena)
email = "MisticusxD@upn.pe"
posicion_arroba = email.find("@")
usuario = email[:posicion_arroba]
dominio = email[posicion_arroba +1 :]
print(f' usuario  : {usuario}')
print(f'dominio : {dominio}')

# Spli

nombre_curso ="BigData y Base de Datos Avanzados"
partes = nombre_curso.split(" ")
print(partes)
print(partes[0])
print(partes[1])
print(partes[2])
print(partes[3])
print(partes[4])
print(partes[5])

# Replace
telefono = "+51-946-645-153"
telefono_clean = telefono.replace("-", "")
print(f'Telefono Limpio : {telefono_clean}')

# UPPER poner a mayusculas

nombre_mayuscula = nombre.upper()
print(nombre_mayuscula)

# LOWER poner a minusculas

nombre_minuscula = nombre.lower()
print(nombre_minuscula)

# strip (espacios en blanco innesesarios al inicio y al final )
palabra = "    Aprendiendo Python      "
palabra_limpia = palabra.strip()

print(f'{palabra_limpia}')