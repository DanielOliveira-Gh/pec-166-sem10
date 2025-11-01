cancao = ''

for i in range(99,251):

    if i == 250:
        cancao += (f'{i} bugs no software, pegue um deles e conserte...\nTecle "Ctrl+F5"\nVamos fazer mais um café!')
    else:
        cancao += str(f'{i} bugs no software, pegue um deles e conserte...\nTecle "Ctrl+F5"\n')
   
print(cancao.strip())

    
