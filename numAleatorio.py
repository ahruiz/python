import random

# generamos un num aleatorio entre 1 y 10, pedir al usuario que lo adivine ingresando un num
print("GENERAMOS UN NUMERO OCULTO ALEATORIO ENTRE EL 1 Y EL 10")

numEscondido = random.randint(1, 10)

numero = int(input("escribe el numero que piensas que se generó: "))

if numero != numEscondido:
    print("Mala suerte!!! Intentalo de nuevo!!!")
else:
    print(f"FELICIDADES.....ganaste un cupon!!!!!")
    
