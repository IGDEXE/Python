# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius
# Ivo Dias

# Recebe a temperatura
farenheit = int(input("Informe o valor em Farenheit: "))

# Faz a conversao
celsius = (5 * (farenheit - 32) / 9)

# Mostra na tela
print("A temperatura em Celsius é",celsius)