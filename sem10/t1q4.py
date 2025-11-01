sequencia = ''
for i in range(10,1001,10):
    if i == 1000:
        sequencia += str(f'{i}.')
    else:
        sequencia += str(f'{i},{" "}')

print(f'Sua sequência de 1000 números de 10 em 10. {sequencia.strip()}')