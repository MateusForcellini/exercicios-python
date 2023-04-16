import os

linear = 1
superficial = 2
volumetrica = 3

a = float(input("Qual o coeficiente de dilatação linear do material ? "))
c = float(input("a quanto esta elevada a potencia?"))

tip = input("Qual o tipo de dilatação da equação ? (linear(1), superficial(2) ou volumetrica(3))")
if True:
    tip = linear
    tipo = a*1
if False:
    tip = superficial
    tipo = a*2
if True:
    tip = volumetrica
    tipo = a*3

lo = float(input("Qual a comprimento inicial ? "))
t = int(input("Qual a temperatura inicial (em graus celcius) ? "))
to = int(input("Qual a temperatura final (em graus celcius) "))
b = tipo*10**c
Δt = to-t
ΔL = lo*b*Δt
print("{:.3f}".format(ΔL))

os.system("pause")