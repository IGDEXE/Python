# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58 | Para mulheres: (62.1*h) - 44.7
# Ivo Dias

# Recebe a altura
altura = int(input("Informe a sua altura: "))

# Calcula o peso
pesoIdealHomem = (72.7 * altura) - 58
pesoIdealMulher = (62.1 * altura) - 44.7

# Mostra na tela
print("Considerando sua altura")
print("Para um homem, o peso ideal é",pesoIdealHomem)
print("Para uma mulher, o peso ideal é",pesoIdealMulher)