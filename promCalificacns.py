#codigo para determinar el promedio de calificaciones
#capturadas por el usuario

totCalif = int(input("cuantas calificaciones quieres capturar: "))
cont = 1      # contador para generar el bucle
calif = []    #generamos una lista vacia para almacenar las calificaciones capturadas


while cont <= totCalif:
    micalif = int(input(f"ingrese la calificacion {cont}: ")) #captura de las calificaciones
    calif.append(micalif) 
    cont += 1
 
prom = round(sum(calif) / len(calif),2)             #redondeamos a dos cifras decimales

print(f"El promedio de mis calificaciones es: {prom}") #se calcula la calif promedio