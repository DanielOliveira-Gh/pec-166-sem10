cancao = ''
for i in range(99,251,7):

    if i + 7 > 250:
        cancao += (f'{i} bugs no software, pegue sete deles e conserte...\nTecle "Ctrl+F5"\nVamos fazer mais um café!')
    else:
        cancao += str(f'{i} bugs no software, pegue sete deles e conserte...\nTecle "Ctrl+F5"\n')
   
print(cancao.strip())