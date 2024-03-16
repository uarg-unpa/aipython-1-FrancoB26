n=int(input("Ingrese un numero entero: "))
primo=True
if n>=0:
    if n<=1:
          print("")
          primo= False
    else:
        for num in range(2,n):
            if n%num==0:
                 print("El numero ingresado no es primo, pero", num, "es divisor")
                 primo=False
    if primo:
        print("El numero ingresado es primo")
    else:
           print("El numero ingresado no es primo")
else:
      print("El numero ingresado no es un numero natural")