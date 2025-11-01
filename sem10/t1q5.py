def maior_de(n):
    maior = 0
    for i in range(n):
        num = int(input(f'Digite {i + 1}° número: '))

        if num > maior:
            maior = num

    return maior

def main():
    num = maior_de(100);
    print(f"O maior numero que você digitou foi {num}")

if __name__ == '__main__':
    main()
