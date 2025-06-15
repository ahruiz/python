#codigo para calcular el indice de masa corporal


peso = float(input("introduce tu peso en Kgs: "))
estatura = float(input("introduce tu estatura en metros: "))

if estatura > 2.2:
    nuevaEstat = estatura / 100 #conversion a metros pensando que capturo en 
    estatura = nuevaEstat

imc = round(peso / (estatura*estatura),2)

print(f"En base a tu peso {peso} y tu estatura {estatura} tienes un IMC de {imc}")

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