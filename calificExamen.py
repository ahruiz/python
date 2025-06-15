#codigo para calificar examenes en base a datos
#proporcionados por el usuario

print("Capturar los datos para calificar tu examen.....") # explicacion del codigo

Preguntas = input("indica el total de preguntas del examen: ")
numaciertos = input("indica el total de aciertos del examen: ")  # pedimos al usr capturar los datos
numfallos  = input("indica el total de fallos del examen: ")

if not Preguntas.isdigit() or not numaciertos.isdigit() or not numfallos.isdigit(): # comprobamos si los datos son correctos
    print("Debes capturar valores numericos enteros y no otro tipo de caracteres")  #advertencia de datos incorrectos
    exit()  # salimos del prog por datos incorrectos

numaciertos = int(numaciertos) # declaramos como enteros las variables que intervienen en la siguiente operacion
Preguntas = int(Preguntas)     #hacemos el num de preguntas dato entero

calif = round((numaciertos / Preguntas) * 100,2)  #calculamos la calificacion redondeado a 2 digitos

print(f"**************************************** Mi calificacion   : {calif}") #mostramos el resultado
