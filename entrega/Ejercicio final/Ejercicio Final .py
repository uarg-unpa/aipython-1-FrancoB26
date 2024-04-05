import random

def lanzar_dado(caras):
    return random.randint(1, caras)

def guardar(caras,cantidad):
    resultados=[ ]
    for num in range(cantidad):
        resultados.append(lanzar_dado(caras))
    return resultados

def total(resultados_lanzamiento):
    suma_de_resultados=0
    for num in resultados_lanzamiento:
        suma_de_resultados=suma_de_resultados+num
    return suma_de_resultados

print("Bienvenido al juego de dados:")
cantidad=int(input("Coloque la cantidad de dados que quiere usar: "))

while cantidad<0 :
    cantidad=int(input("El numero es negativo. Ingrese nuevamente un numero positivo: "))

print("1. Dado numérico de 6 caras")
print("2. Dado numérico de 8 caras")
print("3. Dado numérico de 10 caras")
tipo_de_dado=int(input("Elija el tipo de dado que va a usar: "))

while 0>tipo_de_dado or 3<tipo_de_dado :
    tipo_de_dado=int(input("La opcion ingresada es incorrecta. Elija la opcion que define las caras del dado que va a usar: "))

a=input("Quiere realizar un lanzamiento? (si/no):")
while a=="si" :
    if tipo_de_dado==1:
        print()
        for num in range(cantidad):
            resultados_lanzamiento=guardar(6,cantidad)
        print(f"El lanzamiento fue: {resultados_lanzamiento}")
        print(f"El puntaje total del lanzamiento es: {total(resultados_lanzamiento)}")
        print()
        a=input("Quiere realizar otro lanzamiento? (si/no):")

    elif tipo_de_dado==2 :
        print()
        for num in range(cantidad):
            resultados_lanzamiento=guardar(8,cantidad)
        print(f"El lanzamiento fue: {resultados_lanzamiento}")
        print(f"El puntaje total del lanzamiento es: {total(resultados_lanzamiento)}")
        print()
        a=input("Quiere realizar otro lanzamiento? (si/no):")

    else:
        print()
        for num in range(cantidad):
            resultados_lanzamiento=guardar(10,cantidad)
        print(f"El lanzamiento fue: {resultados_lanzamiento}")
        print(f"El puntaje total del lanzamiento es: {total(resultados_lanzamiento)}")
        print()
        a=input("Quiere realizar otro lanzamiento? (si/no):")
        if a=="no":
            break