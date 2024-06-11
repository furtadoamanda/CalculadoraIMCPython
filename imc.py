print(f"{10 * "*"} CALCULADORA DE IMC {10 * "*"}")

peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em m: "))
imc = peso / (altura ** 2)

imc_normal_minimo = 18.5
peso_ideal_minimo = imc_normal_minimo * (altura ** 2)
imc_normal_maximo = 24.9
peso_ideal_maximo = imc_normal_maximo * (altura ** 2)

if imc < 18.5:
    resultado_imc = "MAGREZA"
elif imc <= 24.9:
    resultado_imc = "NORMAL"
elif imc <= 29.9:
    resultado_imc = "SOBREPESO"
elif imc <= 34.9:
    resultado_imc = "OBESIDADE GRAU I"
elif imc <= 39.9:
    resultado_imc = "OBESIDADE GRAU II"
else:
    resultado_imc = "OBESIDADE GRAU III"


if resultado_imc != "NORMAL":
    print(f"""Seu IMC é de {imc:.2f} Kg/m² ---> {resultado_imc}
Seu peso ideal está entre {peso_ideal_minimo:.2f} Kg e {peso_ideal_maximo:.2f} Kg.
""")
else:
    print(f"Seu IMC é de {imc:.2f} Kg/m² ---> {resultado_imc}")
