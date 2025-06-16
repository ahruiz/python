import random
#funcion para generar num aleatorio

# generamos un num aleatorio entre 1 y 10, pedir al usuario que lo adivine ingresando un num
print("GENERAMOS UN NUMERO OCULTO ALEATORIO ENTRE EL 1 Y EL 10") #explicacion del codigo

numEscondido = random.randint(1, 10) #se genera un num aleatorio oculto

# try:  #manejo de errores........
#     numero = int(input("Escribe el numero que piensas que se generó: "))  #pedimos al usuario que adivine el num

#     if numero != numEscondido:    #comparamos la entrada con el numero oculto y damos la sentencia
#         print("Mala suerte!!! Intentalo de nuevo!!!")
#     else:
#         print(f"FELICIDADES.....ganaste un cupon!!!!!")
# except:
#     print("Los datos capturados no son correctos....") # damos la sentencia de datos incorrectos

numero = input("Escribe el numero que piensas que se genero: ") #pedimos al usr ingresar el num

if not numero.isdigit():  #comprobamos que sea digito
    print("Los datos ingresados son incorrectos......") # damos la sentencia si no l es y salimos del prog
    exit()

numero = int(numero)  #convertimos la variable a entero
if numero < 1 or numero > 10: #comprobamos que este entre 1 y 10
    print("Debes capturar numeros entre 1 y 10.....") # damos la sentencia si no lo esta y salimos del prog
    exit()

if numero != numEscondido:    # comprobamos que la entrada sea diferente del num aleatorio oculto
    print("¡¡¡MALA SUERTE.....Intentalo de nuevo!!!") #damos la sentencia de fallo a ese intento
else:
    print("¡¡¡FELICIDADES!!!....Has ganado un CUPON ") # damos la sentencia de acertado