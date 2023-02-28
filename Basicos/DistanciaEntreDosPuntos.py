# Leer los cuatro valores correspondientes a las coordenadas x e y de dos puntos en el plano, p1 (x1, y1) y p2 (x2, y2)
# y calcular la distancia entre ellos, mostrando cuatro decimales después del punto, de acuerdo a la fórmula:

x1, y1 = input().split()
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

print("{:.4f}".format(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)))


