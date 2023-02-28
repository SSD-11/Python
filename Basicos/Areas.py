# Escriba un programa que lea tres valores de punto flotante: A, B y C. Luego, calcular y mostrar:
# a) El área del triángulo rectángulo de base A y altura C.
# b) El área del círculo de radio C (Pi = 3.14159).
# c) El área del trapecio el cual tiene A y B como bases, y C como altura.
# d) El área del cuadrado de lado B.
# e) El área del rectángulo de lados A y B.

# Entrada
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

# Salida
print("TRIANGULO: {:.3f}".format(a * c / 2))
print("CIRCULO: {:.3f}".format(3.14159 * c ** 2))
print("TRAPEZIO: {:.3f}".format((a + b) * c / 2))
print("QUADRADO: {:.3f}".format(b ** 2))
print("RETANGULO: {:.3f}".format(a * b))