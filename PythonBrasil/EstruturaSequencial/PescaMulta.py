# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.
# Ivo Dias

# Recebe a peso
peso = int(input("Informe a quantidade em KG: "))

# Calcula o excesso
excesso = peso - 50

# Mostra o peso na tela
print("O peso total foi de",peso)

# Verifica se tem multa
if (peso > 50):
    multa = excesso * 4 # Calcula a taxa
    print("Você passou",excesso,"do limite de peso")
    print("O total da multa é",multa) # Mostra na tela
else:
    print("Você está dentro do limite, não existem taxas adicionais")
