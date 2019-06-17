def intervalo():
    p = float(input('Insira o menor valor do intervalo: '))
    for i in range(0, 5):
        m = p+i
        print(m, end=' ')
    c = float(input('\nInsira o valor para comparação: '))
    if m < c or c < p:
        print('O valor não está no intervalo indicado.')
    else:
        print('O valor está no intervalo indicado.')


intervalo()
