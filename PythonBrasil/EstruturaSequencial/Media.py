# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Ivo Dias

# Recebe as notas
primeiroBimestre = int(input("Informe a nota do 1 Bimestre: "))
segundoBimestre = int(input("Informe a nota do 2 Bimestre: "))
terceiroBimestre = int(input("Informe a nota do 3 Bimestre: "))
quartoBimestre = int(input("Informe a nota do 4 Bimestre: "))

# Faz a media
media = (primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre)/4

# Mostra a media
print("A media durante o ano foi",media)