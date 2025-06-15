#codigo para contar las letras de una palabra

print("Vamos a contar las letras de una o varias palabras dadas por el usuario")

texto = input("Introduce un texto o una palabra: ")
espacios  = texto.count(" ")                #contamos los espacios

longtexto = len(texto)

longPalabras = longtexto - espacios                         # obtenemos la longitud del texto sin espacios

print(f"El texto es: [{texto}] y tiene una longitud de {longPalabras} y {espacios} espacios en blanco ")
