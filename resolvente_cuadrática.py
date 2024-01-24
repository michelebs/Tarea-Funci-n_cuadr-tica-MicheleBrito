import math

def la_resolvcuadrática(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        return "No hay raices reales"

# Ejemplo para comprobar
a = 1
b = -3
c = 2

raiz = la_resolvcuadrática(a, b, c)
print(raiz)
