def factorial(a):
    if a<0:
        return "No extiste factorial de un número negativo."
    elif a==0:
        return 1
    else:
        resultado=1
        for num in range(1,a+1):
            resultado=resultado*num
        return resultado
a=int(input("Ingrese un número entero: "))
resultado=factorial(a)
print(f"El factorial de {a} es: {resultado}")