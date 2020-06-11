#Calcular a divisão inteira sem usar o operador de divisão ou função para números inteiros
a = int(input('Digite o divisor: '))
b = int(input('Digite o dividendo: '))
contador = 0
while a>=b:
    a=a-b
    contador +=1
print('O resultado da divisão é ', contador)
