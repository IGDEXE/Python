# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# Ivo Dias

# Recebe o valor
numero = int(input("Informe um numero: "))

# Verifica se é positivo
if (numero > -1):
    print("O numero é positivo")
elif (numero < 0):
    print("O numero é negativo")
else:
    print("Você realmente colocou um numero?")