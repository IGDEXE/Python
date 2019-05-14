# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit
# Ivo Dias

# Recebe a temperatura
celsius = int(input("Informe o valor em Celsius: "))

# Faz a conversao
farenheit = ((celsius / 5) * 9) + 32

# Mostra na tela
print("A temperatura em Farenheit é",farenheit)