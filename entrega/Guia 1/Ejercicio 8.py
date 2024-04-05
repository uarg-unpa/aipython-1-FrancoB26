pi=3.14
a=float(input("Ingrese uno de los lados o base del rectangulo"))
b=float(input("Ingrese el otro lado o altura del rectangulo"))
perimetro=a+b
area=a*b
print(f"El area del rectangulo es {area}", f"su perimetro es{perimetro}")

c=float(input("Ingrese el radio de la circunferencia"))
perimetro2= 2*c*pi
area2=pi*c**2
print(f"El area de la circunferencia es {area2}", f"su perimetro es{perimetro2}")
