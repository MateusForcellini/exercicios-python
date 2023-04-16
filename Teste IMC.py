import os

nome = input("olá, qual o seu nome? ")
p = float(input("Olá {}, digite seu peso em Kg, por favor: ".format(nome)))
a = float(input("{} ,agora, digite sua altura em metros: ".format(nome)))
imc = p/a**2

print("Seu IMC é igual a {:.2f}, {}".format(imc,nome))

if imc < 16:
    print("você está em estado de magreza grave!")

elif imc < 17:
    print("você está em estado de magreza moderada!")

elif imc < 18.5:
    print("você está em estado de magreza leve!")

elif imc < 25:
    print("você está saudável!")

elif imc < 30:
    print("você está em estado de sobrepeso!")

elif imc < 35:
    print("você está em estado de obesidade de primeiro grau!")

elif imc < 40:
    print("Você está em estado de obesidade severa ou de segundo grau!")

else:
    print("Você está com obesidade morbida ou de terceiro grau!")

os.system("pause")