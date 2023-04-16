import math
op = float(input("Qual o comprimentodo cateto oposto ? (metros) "))
adj = float(input("Qual o comprimento cateto adjacente ? (metros) "))
hip = math.hypot(op, adj)
print("A hipotenusa mede {:.2f} metros".format(hip))
