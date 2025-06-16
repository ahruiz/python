import random
#funcion para generar num aleatorio

# generamos un num aleatorio entre 1 y 10, pedir al usuario que lo adivine ingresando un num
print("GENERAMOS UN NUMERO OCULTO ALEATORIO ENTRE EL 1 Y EL 10") #explicacion del codigo

numEscondido = random.randint(1, 10) #se genera un num aleatorio oculto

try:  #manejo de errores........
    numero = int(input("escribe el numero que piensas que se generó: "))  #pedimos al usuario que adivine el num

    if numero != numEscondido:    #comparamos la entrada con el numero oculto y damos la sentencia
        print("Mala suerte!!! Intentalo de nuevo!!!")
    else:
        print(f"FELICIDADES.....ganaste un cupon!!!!!")
except:
    print("Los datos capturados no son correctos....") # damos la sentencia de datos incorrectos
