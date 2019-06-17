def contadorlinha(nomearquivo):
    c = 0
    for line in open(nomearquivo):
        c += 1
    return c

if __name__ == '__main__':
     print('Número de linhas neste arquivo =', contadorlinha('lcount.py'))

print('O valor da variável __name__ é', __name__)