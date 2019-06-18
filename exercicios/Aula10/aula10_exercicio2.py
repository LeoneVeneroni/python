import os

def check():
    for caminho, diretorios, arquivos in os.walk('.'):
        print(caminho)
        print(diretorios)
        print(arquivos)

check()