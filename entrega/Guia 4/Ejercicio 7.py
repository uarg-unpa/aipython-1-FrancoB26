def maximo(a,b,c):
    if a>b>c:
        return a
    elif a<b>c:
        return b
    else :
        return c
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
m=maximo(a,b,c)
print(f"El máximo de los tres números es: {m}")