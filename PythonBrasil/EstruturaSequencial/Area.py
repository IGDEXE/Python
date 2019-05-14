# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# Ivo Dias

# Recebe a biblioteca de calculos
import math

# Recebe o raio
raio = int(input("Informe o raio: "))

# Faz o calculo
area = 2*math.pi*raio

# Mostra na tela
print("A area é",area)