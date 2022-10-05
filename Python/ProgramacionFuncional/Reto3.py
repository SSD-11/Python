def is_prime(n):
    if n == 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True
array = list(map(int, input().split()))
a, b = map(int, input().split())
c, d = map(int, input().split())
if is_prime(array[a]) and is_prime(array[b]):
    print(array[a] + array[b])
else:
    print(array[a] - array[b])
if is_prime(array[c]) and is_prime(array[d]):
    print(array[c] + array[d])
else:
    print(array[c] - array[d])

# # El mismo codigo pero con programacion funcional

from functools import reduce
from operator import add, sub
array = list(map(int, input().split()))
a, b = map(int, input().split())
c, d = map(int, input().split())
print(reduce(add if (array[a] % 2 != 0) and (array[b] % 2 != 0) else sub, [array[a], array[b]]))
print(reduce(add if (array[c] % 2 == 0) and (array[d] % 2 == 0) else sub, [array[c], array[d]]))
