cancao = ''
for i in range(99,0,-11):
# 
    if i - 11 <= 0:    
        cancao += str(f'{i} bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"\nSem erros no software! Está estabilizado!')
    else:
        cancao += str(f'{i} bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"\n')
print(cancao.strip())