#Codigo para pedir 2 numeros, restar al segundo el primero y mostrar si es +, - o cero

num1 = int(input("Ingresa el primer Numero: "))
num2 = int(input("Ingresa el segundoi Numero: "))


totResta = num2 - num1

if totResta < 0:
    print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} y es NEGATIVO")
elif totResta > 0:  
    print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} y es POSITIVO")
else:
    print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} ...cero")
