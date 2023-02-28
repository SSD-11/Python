#Map

lista = [1, 2, 3, 4, 5]
def por_dos(x):
    return x * 2
resultado = map(por_dos, lista)
print(list(resultado)) # [2, 4, 6, 8, 10]

# Con lambdas

lista2 = [1, 2, 3, 4, 5]
resultado2 = map(lambda x: 2 * x, lista2)
print(list(resultado2)) # [2, 4, 6, 8, 10]

# Filter Pares

lista3 = [7, 4, 16, 3, 8]
def es_par(x):
    return x % 2 == 0
pares = filter(es_par, lista3)
print(list(pares)) # [4, 16, 8]

# Con lambdas

lista4 = [7, 4, 16, 3, 8]
pares2 = filter(lambda x: x % 2 == 0, lista4)
print(list(pares2)) # [4, 16, 8]

# Reduce para Suma

from functools import reduce
lista = [1, 2, 3, 4, 5]

suma = reduce(lambda acc, val: acc + val, lista)  # acc = acumulador, val = valor
print(suma)  # 15

# Reduce para suma usando la funcion add

from functools import reduce
from operator import add
lista = [1, 2, 3, 4, 5]
suma = reduce(add, lista)
print(suma)  # 15