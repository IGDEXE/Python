# Faça um Programa que leia três números e mostre o maior deles.
# Ivo Dias

# Recebe os numeros
primeiroNumero = int(input("Informe um numero: "))
SegundoNumero = int(input("Informe um segundo numero: "))
terceiroNumero = int(input("Informe um terceiro numero: "))

# Faz a verificacao
if (primeiroNumero == SegundoNumero) and (primeiroNumero == terceiroNumero):
    print ('Os numeros são iguais')
elif (primeiroNumero > SegundoNumero) and (primeiroNumero > terceiroNumero):
    print ('O maior numero é o:', primeiroNumero)
elif (SegundoNumero > terceiroNumero):
    print ('O maior numero é o:', SegundoNumero)
else:
    print ('O maior numero é o:', terceiroNumero)