# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo | a soma do triplo do primeiro com o terceiro | o terceiro elevado ao cubo
# Ivo Dias

# Importa a biblioteca
import math

# Recebe os numeros
primeiroInteiro = int(input("Informe um numero inteiro: "))
segundoInteiro = int(input("Informe um outro numero inteiro: "))
numeroReal = int(input("Informe um numero real: "))

# Faz as contas
primeiraConta = (2 * primeiroInteiro) * (segundoInteiro / 2)
segundaConta = (3 * primeiroInteiro) + numeroReal
terceiraConta = math.pow(numeroReal, 3)

# Mostra na tela
print("Produto do dobro do primeiro com metade do segundo:",primeiraConta)
print("Soma do triplo do primeiro com o terceiro:",segundaConta)
print("Terceiro elevado ao cubo:",terceiraConta)