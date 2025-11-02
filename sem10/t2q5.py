# recebendo os dados de entrada
preco_total = float(input('Digite o valor da compra: '))

# laço de repetição com for para calcular valor da parcela
for i in range(1,25):
    valor_parc = preco_total / i
# siada de dados com a simulação das parcelas
    print(f'Veja a simulação em até 24x.\n{i}x de R$ {valor_parc:.2f}')
