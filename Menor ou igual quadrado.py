#Mostra o menor ou igual quadrado de um número, calculando a raiz por subtrações
n = int(input('n: '))
x=n
impar=1
while x>0:
    x= x-impar
    impar+=2
    if x==0:
        print('O quadrado é: %d' % n)
        break
    elif x<0:
        n-=1
        x=n
        impar=1
        
    

