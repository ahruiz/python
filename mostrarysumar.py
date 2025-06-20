#Codigo para pedir 2 numeros, sumarlos y mostrarlos

print("Codigo para mostrar la suma de dos numeros dados por el usuario....")

num1 = input("ingresa el primer numero: ")
num2 = input("ingresa el segundo numero: ") #pedimos al usr ingresar los datos

if not num1.isdigit() or not num2.isdigit(): #verificamos q la entradas sean enteros
    print("Los valores capturados no son correctos.....") # advertimos el error y cerramos 
    exit()  

num1 = int(num1)  # Convertimos las cadenas a enteros
num2 = int(num2)  

totSuma = num1 + num2 #efectuamos la operacion

print(f"Los numeros capturados son {num1} y {num2} y la suma de ambos es {totSuma}") #mostramos los datos
