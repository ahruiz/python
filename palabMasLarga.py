"""codigo para determinar la pañabra mas larga de un texto
ingresado por el usuario"""
from colorama import Fore

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# print("------- Codigo para determinar la palabra mas larga de un texto -------") #explicacion del codigo

# mitexto = input("Ingresa el TEXTO a analizar....: ") #pedimos al usuario ingresar el texto

# palabras = mitexto.split() #generamos un diccionario con las palabras del texto ingresado

# longTxt = len(palabras) # determinamos la long del diccionario, es decir, cuantas palabras tiene

# longMasLarga = max(len(palabra) for palabra in palabras)
# """ la funcion max determina, de los integrantes del diccionario, cual es la mas grande
# en base a las longitudes de cada una de las palabras"""

# palMasLarga = {palabra for palabra in palabras if len(palabra) == longMasLarga} 
# """ la sentencia obtiene un str, por lo tanto es un objeto y como lleva varias sentencias
#     no se puede poner entre()
#     en el diccionario se checa palabra x palabra la longitud y 
#     se almacena la que concida con la longitud mas larga"""
    
# print(f" mi texto es : {palabras} con {longTxt} palabras") # mostramos los resultados
# print(f"la palabra mas larga es {palMasLarga} con una longitud de {longMasLarga}")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# print("------- Codigo para determinar la palabra mas larga de un texto -------") #explicacion del codigo

# mitexto = input("Ingresa el TEXTO a analizar....: ") #pedimos al usuario ingresar el texto

# palabras = mitexto.split() #generamos un diccionario con las palabras del texto ingresado

# longTxt = len(palabras) # determinamos la long del diccionario, es decir, cuantas palabras tiene
# palMasLarga = max(palabras, key = len) 
# """de todas las palaras del dicc "palabras" determina cual es la mayor en funcion de la llave:longitud
#    pero guarda la palabra, no la longitud"""
# longMasLarga = len(palMasLarga)
# """ aqui solo sacamos la longitud de la palabra mas larga"""

# print(f" mi texto tiene {longTxt} palabras..... y") # mostramos los resultados
# print(f"la palabra mas larga es {palMasLarga} con una longitud de {longMasLarga}")

print("------- Codigo para determinar la palabra mas larga de un texto -------") #explicacion del codigo

mitexto = input("Ingresa el TEXTO a analizar....: ") #pedimos al usuario ingresar el texto

palabras = mitexto.split() #generamos un diccionario con las palabras del texto ingresado
espaciosBco = mitexto.count(" ")

miDicc= {}
#for i, elemento in enumerate(palabras):
#   miDicc[i] = elemento     ESTE CICLO INCLUYE EL INDICE, AA CADA ELEMENTO LE CREA UN INDICE
#for i, elemento in enumerate(palabras): # enumerate solo se usa para incluir el indice, osea, "i"

for elemento in palabras: #en este caso no tenemos "i", no usamos enumerate, porque no incluiremos el valir de "i"
    miDicc[elemento] = len(elemento) #mi dicc se compone de cada uno de los elementos como clave
                                     # y la longitud de cada elemento como valor

longTxt = len(palabras)
palMasLarga = max(miDicc, key = len)
longMasLarga = len(palMasLarga)

print(f" mi texto tiene {longTxt} palabras, ademas de {espaciosBco} espacios en blanco..... y") # mostramos los resultados
print(f"la palabra mas larga es {Fore.YELLOW} {palMasLarga} {Fore.WHITE} con una longitud de {longMasLarga} letras")
