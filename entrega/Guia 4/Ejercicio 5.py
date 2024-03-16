def parimpar(numero):
    if numero%2==0:
        return "El numero es par"
    else:
        return "El numero es impar"
numero=int(input("Ingrese un numero: "))
print(parimpar(numero))