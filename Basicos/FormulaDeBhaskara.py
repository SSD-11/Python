# Leer 3 números de punto flotante. Luego, imprimir las raíces de la fórmula de Bhaskara. Si es imposible calcular
# las raíces debido a una división por cero ó a la raíz cuadrad de un número negativo, presentar el mensaje “Impossivel calcular”.

a, b, c = list(map(float, input().split()))
D = b * b - 4 * a * c
E = pow(D, .5)
if (D < 0 or a == 0):
    print("Impossivel calcular")
else:
    f = (-b + E) / (2 * a)
    g = (-b - E) / (2 * a)
    print("R1 = %.5lf" % f)
    print("R2 = %.5lf" % g)
