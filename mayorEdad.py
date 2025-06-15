#codigo para diferenciar peliculas de acuerdo a la edad
from colorama import Fore

print("Mostrar peliculas de acuerdo a la edad") # explicacion del codigo

peliculas = {"EL EXORCISTA": "R", "BLANCA NIEVES":"A", "DESTINO FINAL":"R", "LA SIRENITA":"A"}

#*************************************************** estas sentencias no arrojan formato de dicc
edad = int(input("Captura tu edad para mostrarte la cartelera: "))

if edad < 18:
    print(f"{Fore.YELLOW} La cartelera para menores de 18 años es:  {Fore.WHITE}")
    for clave, valor in peliculas.items():
        if valor == "A":
            print(clave)
else:
    print(f"{Fore.YELLOW} La cartelera para mayores de 18 años es:  {Fore.WHITE}")    
    for clave, valor in peliculas.items():
        print(clave)

#***************************************************** entrega formato de diccionario(parametros de dicc en INGLES)
# edad = int(input("Captura tu edad para mostrarte la cartelera: "))

# if edad < 18:
#     cartelMen = [k for k,v in peliculas.items() if v == "A"]
#     print(f"{Fore.YELLOW}La cartelera para menores de 18 años es: {cartelMen} {Fore.WHITE}")
# else:
#     cartelMay = [key for key,value in peliculas.items()]
#     print(f"{Fore.YELLOW}La cartelera para mayores de 18 años es: {cartelMay} {Fore.WHITE}")


#***************************************************** entrega formato de diccionario(parametros de dicc en ESPAÑOL)
# edad = int(input("Captura tu edad para mostrarte la cartelera: "))

# if edad < 18:
#     cartelMen = [clave for clave,valor in peliculas.items() if valor == "A"]
#     print(f"{Fore.YELLOW}La cartelera para menores de 18 años es: {cartelMen} {Fore.WHITE}")
# else:
#     cartelMay = [clave for clave,valor in peliculas.items()]
#     print(f"{Fore.YELLOW}La cartelera para mayores de 18 años es: {cartelMay} {Fore.WHITE}")


#******************************************************* varible por pelicula
# pelicula1 = "Halloween 5"
# pelicula2 = "Sonic"
# pelicula3 = "Walking Dead"
# pelicula4 = "Laguna Azul"

# edad = int(input("Indicanos que edad tienes: "))

# pelicAdulto = pelicula1 + ' y ' + pelicula3
# pelicMenores = pelicula2 + ' y ' + pelicula4

# if edad < 18:
    
#     print(f" Cartelera para menores de 18: {pelicMenores}")
# if edad > 18:
#     print(f" Cartelera para mayores de edad: {pelicMenores} ademas de {pelicAdulto}")

