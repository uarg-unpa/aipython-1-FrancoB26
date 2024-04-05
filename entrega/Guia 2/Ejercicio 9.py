edad=int(input("Ingrese su edad: "))

if 18<=edad :
    ingreso=int(input("Ingrese su ingreso mensual: "))
    if ingreso>100000 :
        print("Usted tiene que pagar el impuesto")
    else :
        print("Usted no tiene  que pagar el impuesto")
else:
    print("Usted es menor de edad")