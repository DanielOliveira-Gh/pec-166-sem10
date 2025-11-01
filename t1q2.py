# variaveis auxiliares
pares = 0
impares = 0

# entrada de dados 100 números
for i in range(1,101):
    numero = int(input())
# verificar se e par ou impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
# saida de dados
print(pares)
print(impares)