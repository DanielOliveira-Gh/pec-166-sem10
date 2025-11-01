soma = 0
for i in range(1, 101):
    num = int(input(f'Digite {i}° número: '))
    soma += num

media = soma / 100

print(f'A média dos 100 números é {media}')