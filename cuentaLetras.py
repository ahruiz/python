#codigo para contar las letras de una palabra

print("Vamos a contar las letras de una o varias palabras dadas por el usuario") #explicacion del codigo

texto = input("Introduce un texto o una palabra: ") #pedimos al usuario capturar los datos
espacios  = texto.count(" ")                #contamos los espacios

longtexto = len(texto) #sacamos la long del texto

longPalabras = longtexto - espacios                         # obtenemos la longitud del texto sin espacios

print(f"El texto es: [{texto}] y tiene una longitud de {longPalabras} y {espacios} espacios en blanco ")
#mostramos los resultados