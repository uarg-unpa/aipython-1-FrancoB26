import math
A=float(input("Ingrese uno de los lados o base del rectangulo"))
B=float(input("Ingrese el otro lado o altura del rectangulo"))
perimetro=A+B
area=A*B
print(f"El area del rectangulo es {area}", f"su perimetro es{perimetro}")

C=float(input("Ingrese el radio de la circunferencia"))
perimetro2= 2*C*math.pi
area2=math.pi*C**2
print(f"El area de la circunferencia es {area2}", f"su perimetro es{perimetro2}")
