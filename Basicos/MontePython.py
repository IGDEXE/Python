# Ivo Dias
# Exemplo de estrutura basica

# Importando as bibliotecas
import random

# Faz as boas vindas
print("Bem vindo ao monte Python!")
print("Para passar pela ponte, precisa responder 3 perguntas!")

# Recebe as informacoes
nome  = input("Qual o seu nome? ")
missao = input("Qual a sua missao? ")

# Gera um numero aleatorio para definir a dificuldade
dificuldade = random.randint(1,10)

# Se a dificuldade for maior que 7, faz a pergunta lendaria
if (dificuldade > 7):
    ultimaPergunta = input("Qual a velocidade de uma andorinha sem carga? ")
    # Obviamente, ela só pode ser respondida com uma outra pergunta lendaria
    if (ultimaPergunta == "Uma andorinha europeia ou africana?"):
        texto = "Voce me pegou, aaah...(o anciao eh jogado pelo desfiladeiro...)"
    else:
        texto = "Voce errou, em vez de passar por essa ponte, assista Monte Python"
# Caso seja sortudo, vai passar com uma facil
else:
    ultimaPergunta = input("Qual a sua cor favorita? ")
    texto = ("Ooh, Sir %s, cuja a missao eh %s e a cor favorita %s, pode seguir seu caminho" % (nome, missao, ultimaPergunta))

# Escreve na tela
print(texto)