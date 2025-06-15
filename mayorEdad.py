#codigo para diferenciar peliculas de acuerdo a la edad

print("Mostrar peliculas de acuerdo a la edad")

pelicula1 = "Halloween 5"
pelicula2 = "Sonic"
pelicula3 = "Walking Dead"
pelicula4 = "Laguna Azul"

edad = int(input("Indicanos que edad tienes: "))

pelicAdulto = pelicula1 + ' y ' + pelicula3
pelicMenores = pelicula2 + ' y ' + pelicula4

if edad < 18:
    
    print(f" Cartelera para menores de 18: {pelicMenores}")
if edad > 18:
    print(f" Cartelera para mayores de edad: {pelicMenores} ademas de {pelicAdulto}")

