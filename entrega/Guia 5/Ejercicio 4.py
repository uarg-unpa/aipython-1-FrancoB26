lista_frutas=[]
for num in range(5):
    fruta=input("Ingrese su fruta favorita: ")
    lista_frutas.append(fruta)
print("Sus frutas favoritas son: ", lista_frutas)

l=len(lista_frutas)
print("La longitud de la lista es:",l)

frutas2=lista_frutas[1:]
print(frutas2)

print("Se agregara a la lista las uvas como fruta favorita: ")
lista_frutas.append("Uvas")
print(lista_frutas)

