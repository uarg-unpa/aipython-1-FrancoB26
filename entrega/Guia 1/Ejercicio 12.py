cantinvert=float(input("Ingrese la cantidad a invertir: "))
intanual=float(input("Ingrese el interés anual (en porcentaje): "))
años=int(input("Ingrese el número de años: "))
tasainteres=intanual/100
capitalobtenido=cantinvert*(1+tasainteres)**años
print("El capital obtenido de la inversión es:", capitalobtenido)

