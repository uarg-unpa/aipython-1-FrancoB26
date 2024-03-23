palabras_favoritas=[]
for num in range(4):
    palabra=input("Ingrese su palabra favorita: ")
    palabras_favoritas.append(palabra)

sublista=palabras_favoritas[1:4]
print("La sublista desde la segunda palabra hasta la cuarta seria:", sublista)