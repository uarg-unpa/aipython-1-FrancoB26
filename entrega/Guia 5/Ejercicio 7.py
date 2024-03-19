lista=[]
for num in range(5):
    compañia=input("Ingrese el nombre sus compañias favoritas: ")
    lista.append(compañia)
print("Sus compañias favoritas son: ", lista)


a=len(lista)
indice=1
for num in range(a):
    indice=indice+1
    print(f"{indice}. {lista[num]}")


b=int(input("Cual compañia se desea modificar: "))
nombre_editado=input("Ingrese la edicion de la compañia: ")
lista[b]=nombre_editado
print(lista)