def f_c(a):
    g_c=(a-32)*5/9
    return g_c
b=float(input("Ingrese la temperatura en gfrados fahrenheit: "))
celsius=f_c(b)
print(f"{b} grados fahrenheit son equivalentes a {celsius} grados Celsius.")
