def invertir(palabra):
    return palabra[ : : -1]

palabra=input("Ingrese un texto o palabra: ")
invertir=invertir(palabra)
print("El texto invertido es: ", invertir)