# Faça um Programa que peça dois números e imprima o maior deles.
# Ivo Dias

# Recebe os numeros
primeiroNumero = int(input("Informe um numero: "))
segundoNumero = int(input("Informe um outro numero: "))

# Verifica o maior
if (primeiroNumero > segundoNumero):
    print("O primeiro numero é maior que o segundo")
elif (segundoNumero > primeiroNumero):
    print("O segundo numero é maior que o primeiro")
elif (primeiroNumero == segundoNumero):
    print("Os numeros são iguais")
else:
    print("Você realmente colocou um numero?")