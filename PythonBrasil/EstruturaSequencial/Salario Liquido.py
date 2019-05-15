# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido
# Ivo Dias

# Recebe a remuneracao
remuneracao = int(input("Quanto você ganha por hora? "))

# Recebe as horas
horas = int(input("Quantas horas você trabalha? "))

# Calcula o salario bruto
salarioBruto = remuneracao * horas

# Calcula os descontos
impostoRenda = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = impostoRenda + INSS + sindicato

# Calcula o salario liquido
salarioLiquido = salarioBruto - descontos

# Mostra na tela
print("+ Salario Bruto : R$",salarioBruto)
print("- IR (11%) : R$",impostoRenda)
print("- INSS (8%) : R$",INSS)
print("- Sindicato ( 5%) : R$",sindicato)
print("= Salario liquido : R$",salarioLiquido)