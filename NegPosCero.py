#Codigo para pedir 2 numeros, restar al segundo el primero y mostrar si es +, - o cero

print("Codigo para pedir 2 numeros, restar al segundo el primero y mostrar si es +, - o cero")

# try:    #************************************ciclo de intrucciones con manejo de errores
#     num1 = int(input("Ingresa el primer Numero: "))
#     num2 = int(input("Ingresa el segundoi Numero: "))

#     totResta = num2 - num1
#     if totResta < 0:
#         print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} y es NEGATIVO")
#     elif totResta > 0:  
#         print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} y es POSITIVO")
#     else:
#         print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} ...cero")
# except:
#     print("Los datos capturados no son correctos......")

#************************************ciclo de intrucciones con comprobacion de datos
num1 = input("Ingresa el primer Numero: ")
num2 = input("Ingresa el segundo Numero: ") #solicitamos los datos al usuario

if not num1.isdigit() or not num2.isdigit():   # comprobamos que las entradas no sean diferentes de digitos
    print("Los datos capturados no son correctos......")  # si son diferentes solo damos la aclaracion
else:
    num1 = int(num1) #llevamos los datos a enteros
    num2 = int(num2)
    totResta = num2 - num1 #para poder efectuar operaciones
    
    if totResta < 0:   # definimos si son neg, pos o cero
        print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} y es NEGATIVO")
    elif totResta > 0:  
        print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} y es POSITIVO")
    else:
        print(f"Los numeros capturados son {num1} y {num2}...su resta es {totResta} ...cero")
    