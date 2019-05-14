# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
# Ivo Dias

# Recebe a remuneracao
remuneracao = int(input("Quanto você ganha por hora? "))

# Recebe as horas
horas = int(input("Quantas horas você trabalha? "))

# Calcula o salario
salario = remuneracao * horas

# Mostra na tela
print("O seu salario nesse mes é",salario)