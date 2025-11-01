# variável auxiliar
cancao = ''
# estrutura de repetição com for
for i in range(99,251):
# verificação da condicional composta
    if i % 2 != 0:
        cancao += str(f'{i} bugs no software, pegue um deles e conserte...\n')
    else:
        cancao += str(f'{i} bugs no software, pegue um deles e conserte...\n')
# saida de dados
print(f'Cação do Programador {cancao.strip()}')
