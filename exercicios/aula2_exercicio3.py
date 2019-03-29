print('Um livro custa 24.95 reais')
print('As livrarias têm desconto de 40%')
print('Os custos de envio são de 3.00 reais para o primeiro livro')
print('Os custos de envio são de 0.75 reais para os livros adicionais')
print('Qual é o custo total da compra de 60 livros?')

L=24.95
d=0.4
c1=3.00
c2=0.75
T=L-d*L
T1=T+c1
T2=59*T+0.75*59
TT=T1+T2

print('=======================================')
print('Custo total =', TT)