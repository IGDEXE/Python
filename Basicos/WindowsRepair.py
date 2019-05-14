# Ivo Dias
# Ferramenta de reparo

# Importa as bibliotecas
import os

# Define os comandos
cmd = ["@echo off","cls","title Reparo do Windows","sfc /scannow","dism /online /cleanup-image /restorehealth","color 27","pause"]

# Cria um laço para executar os comandos
for item in cmd:
    os.system(item)