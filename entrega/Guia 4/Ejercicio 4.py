def tabla(numero):
    for num in  range(1,11):
        producto=numero*num
        print(f"{numero} x {num} = {producto}")

numero=int(input("Ingrese un numero: "))
print(tabla(numero))