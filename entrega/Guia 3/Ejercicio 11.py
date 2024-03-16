n=int(input("Ingrese un numero: "))
for num in range(1,n+1,2):
    for numero in range(num,0,-2 ):
        print(numero,end=" ")
    print("")