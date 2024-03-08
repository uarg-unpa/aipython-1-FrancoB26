dia=int(input("Ingrese un numero: "))

if 1<=dia<=7 :
    if dia==1:
        print("El numero corresponde al dia Lunes")
    elif dia==2:  
        print("El numero corresponde al dia martes")
    elif dia==3:  
        print("El numero corresponde al dia miercoles")
    elif dia==4:  
        print("El numero corresponde al dia jueves")
    elif dia==5:  
        print("El numero corresponde al dia viernes")
    elif dia==6:  
        print("El numero corresponde al dia sabado")
    else:
        print("El numero corresponde al dia domingo")
else :
    print("El numero que ingreso no corresponde a ningun dia")