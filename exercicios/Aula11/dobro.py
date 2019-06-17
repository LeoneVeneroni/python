class Dobro:

    def dobrar_elementos(uma_lista):
        """ Reescreve os elementos de uma_lista com o dobro de seus valores originais, preservando os elementos da lista original
        """
        nova_lista = []
        for valor in uma_lista:
            novo_elem = 2 * valor
            nova_lista.append(novo_elem)

        return nova_lista


print('__name__ =', __name__)

if __name__ == '__main__': # __name__ = __main__ quando eu rodar esse programa, e __name__ = 'nome do arquivo importado'
    # se eu importar esse script para outro script
    minha_lista = [2, 4, 6]
    print(minha_lista)
    print(Dobro.dobrar_elementos(minha_lista))
