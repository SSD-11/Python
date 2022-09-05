# CALCULO SIMPLE

#Entrada
a1, b1, c1 = input().split()
a2, b2, c2 = input().split()

a1 = int(a1)
b1 = int(b1)
c1 = float(c1)

a2 = int(a2)
b2 = int(b2)
c2 = float(c2)

#Salida
print("VALOR A PAGAR: R$ {:.2f}".format(b1 * c1 + b2 * c2))