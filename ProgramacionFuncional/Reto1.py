T = int(input())
for i in range(T):
    array = list(map(int, input().split()))
    a, b = map(int, input().split())
    print(array[a] + array[b])

# El mismo codigo pero con programacion funcional

from functools import reduce
from operator import add

T = int(input())
for i in range(T):
    array = list(map(int, input().split()))
    a, b = map(int, input().split())
    print(reduce(add, [array[a], array[b]]))
