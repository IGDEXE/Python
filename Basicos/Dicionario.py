# Ivo Dias
# Exemplo de dicionario

# Importa as bibliotecas
import sys

# Faz as boas vindas
print("Bem vindo ao monte Python!")
print("Vamos alistar voce, para isso, responda as perguntas")
print("Afinal, nao podemos recrutar uma bruxa...")

# Recebe os dados
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
peso = input("Qual o seu peso? ")
habilidade = input("Qual a sua principal habilidade? ")
frase = input("Qual sua frase de efeito? ")

# Confirma se ele nao eh uma bruxa
if (peso == "igual ao de um pato"):
    print("Ooh, voce eh uma bruxa, vamos leva-lo a fogueira...")
    print("Antes que torne um de nos em uma lagartixa, novamente....")
    sys.exit()
# Ou se nao eh um lendario cavaleiro
elif (frase == "Eh so um arranhao"):
    print("Acho que ja te conheco..")
    nome = "Cavaleiro Negro"
else:
    print("Ooh, que ordinario")

# Cria o dicionario
pessoa = {
    "nome" : nome,
    "idade" : idade,
    "peso" : peso,
    "habilidade" : habilidade,
    "frase" : frase
}

# Retorna na tela
print("Ok sir %s, cuja a idade eh de %s anos, espero, e que pesa %s arrobas." % (pessoa['nome'], pessoa['idade'], pessoa['peso']))
print("Aproveitaremos sua grande habilidade(sera mesmo??) %s" % (pessoa['habilidade']))
print("E se possivel, pare de falar '%s'" % (pessoa['frase']))