edad1=int(input("Ingrese su edad: "))
edad2=21
if edad1>edad2 :
    añosdediferencia=edad1-edad2
    if añosdediferencia==1:
        print("Hay un año más que mis 21 años.")
    else:
        print(f"Hay {añosdediferencia} años más que mis 21 años.")
elif edad1<edad2:
    añosdediferencia=edad2-edad1
    if añosdediferencia==1:
        print("Hay un año menos que mis 21 años.")
    else :
        print(f"Hay {añosdediferencia} años menos que mis 21 años.")
else :
    print("Tenemos la misma edad")

