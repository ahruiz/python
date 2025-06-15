#codigo para calcular el indice de masa corporal

print("CAlcular el IMC en base a peso y estatura.....")    #explicacion del codigo

peso = float(input("introduce tu peso en Kgs: ")) #pedimos al usr capt los datos
estatura = float(input("introduce tu estatura en metros: "))  # y se definen variables float  al mismo tiempo

if estatura > 2.2: #comprobamos que la captura sea en metros, sino se cumple, seguimos con el proceso
    nuevaEstat = estatura / 100 #conversion a metros pensando que capturo en centimetros
    estatura = nuevaEstat   #damos el valor nuevo a la variable en metros

imc = round(peso / (estatura*estatura),2)   #Calculamos el IMC y lo redondeamos a dos digitos

print(f"En base a tu peso {peso} y tu estatura {estatura} tienes un IMC de {imc}")
#mostramos los datos del IMC y una ADVERTENCIA sobre su situacion

if imc <= 18.5:
    print("BAJO PESO....debes comer mas")
elif imc > 18.5 and imc < 24.9:
    print("PESO NORMAL...sigue manteniendo ese ritmo")
elif imc > 25.0 and imc < 29.9:
    print("SOBREPESO....wacha lo que comes.... seguro que algo de chatarra")
elif imc > 30.0 and imc < 34.9:
    print("OBESIDAD tipo I.....aguas, poca comida nutritiva y poco ejecicio.....empieza a preocuparte")
elif imc > 35.0 and imc < 39.9:
    print("OBESIDAD tipo II....definitivo....no estas cuidando lo que comes....ya bajale")
else:
    print("OBESIDAD tipo III....al medicooooo, te esta cargando pifas")