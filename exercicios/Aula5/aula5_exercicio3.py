def mult():
    A = list()
    for c in range(0, 5):
        A.append(int(input('Digite um valor para a lista: ')))

    B = A[0]*A[1]*A[2]*A[3]*A[4]    
    print('Produto dos números da lista =', B)
    
mult()