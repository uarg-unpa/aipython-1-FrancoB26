n=int(input("Ingrese un numero: "))
suma=0
for num in range(1,n+1) :
    suma=suma+num
    if num==n:
        print(num, end=" = ")
    else :
        print(num, "+", end=" ")
print(suma, end=" ")