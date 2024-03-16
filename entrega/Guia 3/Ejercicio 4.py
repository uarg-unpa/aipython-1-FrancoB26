n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro numero: "))
if n1<n2 :
    for numero in range(n1+1,n2):
        print(numero)
else :
    for numero in range(n2-1,n1):
        print(numero)