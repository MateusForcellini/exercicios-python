import PySimpleGUI as sg

    sg.theme('Default 1') #tema

#layout base do programa
layout = [[sg.Text("Olá, qual o seu peso ? (em kg)")],
    [sg.InputText(key="peso")],
    [sg.Text("E sua altura ? (em metros)")],
    [sg.InputText(key="altura")],
    [sg.Text("", key="IMC")], [sg.Text("", key="mensagem")],
    [sg.Button("continuar")],
    [sg.Button("cancelar")],
]
#nome da janela
janela = sg.Window("Teste de IMC",layout)
# variaveis/abrir e fechar janela
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == "cancelar":
        break

    p = float(valores["peso"])
    a = float(valores["altura"])
    imc = p / a ** 2

#condições do resultado

    if imc < 16:
        resultado = 'com magreza grave'

    elif imc < 17:
        resultado = 'com magreza moderada'

    elif imc < 18.5:
        resultado = 'com magreza leve'

    elif imc < 25:
        resultado = 'saudavel'

    elif imc < 30:
        resultado = 'com sobrepeso'

    elif imc < 35:
        resultado = 'com obesidade I'

    elif imc < 40:
        resultado = 'com obesidade II'

    else:
        resultado = 'com obesidade morbida ou obesidade III'

#cauculo/mais variaveis e conta

    if evento == "continuar":
        p = float(valores["peso"])
        a = float(valores["altura"])
        imc = p/a**2
        janela["IMC"].update(f"O seu imc é igual a {imc:.4f}")
        janela["mensagem"].update(f"Você está {resultado}")

janela.close()