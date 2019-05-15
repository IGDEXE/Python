# Faça um Programa que verifique se uma letra digitada é vogal ou consoante
# Ivo Dias

# Recebe a letra
letra = input("Informe uma letra: ")

# Faz a verificação
if ('AEIOU'.find(letra.upper()) >= 0):
    print("VOGAL")
else:
    print("CONSOANTE")