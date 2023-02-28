# Hacer un programa que lea 3 valores enteros y presente el mas grande seguido del mensaje "eh o maior"
# . Usando la siguiente fórmula.

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print(a, "eh o maior")
elif b > a and b > c:
    print(b, "eh o maior")
else:
    print(c, "eh o maior")
