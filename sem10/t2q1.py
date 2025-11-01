# variável auxiliar
cancao = ''
# estrutura de repetição com for
for i in range(99,251):
# adicionando a string na variável auxiliar
    cancao += str(f'{i} bugs no software, pegue um deles e conserte...\n')
    
# saida de dados
print(f'Cação do Programador.\n{cancao.strip()}')
