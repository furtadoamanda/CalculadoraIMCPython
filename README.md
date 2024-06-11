# Calculadora IMC com Python ⚖️🐍

Criei esse projeto para praticar os conhecimentos de Python.  
É um programa simples que calcula o IMC do usuário de acordo com as informações passadas por ele, informando se este está nos limites do peso ideal ou em outra categoria.

### Parte inicial do código:

```python
print(f"{10 * "*"} CALCULADORA DE IMC {10 * "*"}")

peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em m: "))
imc = peso / (altura ** 2)
```
Inicialmente, é exibida uma mensagem de boas-vindas ao programa, sendo logo solicitado que o usuário insira seu peso em Kg e sua altura em metros. É utilizada a função *float()* para converter a entrada do usuário em um número com ponto flutuante.

### Cálculo do peso ideal:

```python
imc_normal_minimo = 18.5
peso_ideal_minimo = imc_normal_minimo * (altura ** 2)
imc_normal_maximo = 24.9
peso_ideal_maximo = imc_normal_maximo * (altura ** 2)
```
Nesse trecho de código são calculados os pesos máximos e mínimos dentro dos limites do IMC normal, caracterizando os máximos e mínimos valores para o peso ideal.  
Aqui, importante pontuar que são definidas as variáveis *imc_normal_minimo* e *imc_normal_maximo* para fins de tornar o código mais legível, ficando claro ao leitor a que os valores 18.5 e 24.9 são referentes.

### Blocos if:

```python
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
```
O presente bloco *if* atribui à variável *resultado_imc* as categorias de classificação definidas pela OMS, de acordo com o valor obtido pelo cálculo do IMC.

```python
if resultado_imc != "NORMAL":
    print(f"""Seu IMC é de {imc:.2f} Kg/m² ---> {resultado_imc}
Seu peso ideal está entre {peso_ideal_minimo:.2f} Kg e {peso_ideal_maximo:.2f} Kg.
""")
else:
    print(f"Seu IMC é de {imc:.2f} Kg/m² ---> {resultado_imc}")
```
O segundo bloco if é o principal bloco de código do programa. Nele, caso a variável *resultado_imc* seja diferente de normal, ou seja, fora do peso ideal, será exibida a mensagem de saída indicando o valor do IMC e a categoria na qual o usuário se encontra, sendo ainda informado os valores máximo e mínimo do peso ideal de acordo com sua altura.  
Por outro lado, caso o usuário esteja dentro da categoria normal, será apenas informado o valor do IMC e a categoria.