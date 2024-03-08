n=int(input("Ingrese la nota del alumno: "))
if 80<= n <=100 :
    print("Nota A")
elif 70<=n<=79:  
        print("Nota B")
elif 60<=n<=69 :  
            print("Nota C")
elif 50<=n<=59:  
            print("Nota D")
elif 0<=n<=49 :
            print("Nota F")
else :
    print("La nota que ingreso esta fuera del rango 0-100")