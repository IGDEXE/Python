# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "c", se a média for igual a dez.
# Ivo Dias

# Recebe as notas
primeiraNota = int(input("Informe a primeira nota: "))
segundaNota = int(input("Informe a segunda nota: "))

# Calcula a media
media = (primeiraNota + segundaNota) / 2

# Verifica a media
if (media < 7):
    nota = "Reprovado"
elif (media == 10):
    nota = "Aprovado com Distinção"
elif (media >= 7):
    nota = "Aprovado"
else:
    print("As informações não são validas")

# Mostra na tela
print(nota)