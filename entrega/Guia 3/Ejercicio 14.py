a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
if a<b :
    for num in range(a,b+1):
        if num%2==0:
            print(num)
else:
    for num in range(b,a-1):
        if num%2==0:
            print(num)