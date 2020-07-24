def identidade (a,m,n): #m- linha n-coluna
    diagonal=0
    resto=0
    for i in range (m): #percorre a linha
        for j in range (n):
            if i==j and a[i][j] == 1: #verifica a diagonal principal
                diagonal+=1
            if i!=j and a[i][j] ==0:
                resto+=1
    if diagonal==m and resto== m*m-n:
        return True
        return False

def preenche (a,m,n):  #preenche a matriz
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input('a [ %d ][ %d ]: ' % (i,j)))
        print(' ')

while True: #enquanto a matriz n for quadrada
    m = int(input('Digite a quantidade de linhas: '))
    n = int(input('Digite a quantidade de colunas: '))
    if m>0 and m==n:
        break
    else:
        print("Digite uma matriz quadrada positiva.")
    
a=[[0 for j in range (n)] for i in range (m)]
preenche(a,m,n)
print('A sua matriz é identidade? ')
print(identidade(a,m,n))


    
        
