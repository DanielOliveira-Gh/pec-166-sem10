# variável auxiliar
sequencia = ''
# estrutura de repetição com for 
for i in range(10,1001,10):
# verificação da condicional
    if i == 1000:
        sequencia += str(f'{i}.')
    else:
        sequencia += str(f'{i},{" "}')
# saida de dados
print(f'Sua sequência de 1000 números de 10 em 10.\n{sequencia.strip()}')
