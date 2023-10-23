def rotate(s, k):
    return s[k:] + s[:k]


T = int(input())
for i in range(T):
    k, s = input().split()
    k = int(k)
    print(rotate(s, k), end=" ")
