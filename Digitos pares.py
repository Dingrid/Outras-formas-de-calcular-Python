#Mostra a quantidade de alagarismos pares existentes no número digitado, para numero>0
numero=int(input('Digite um número: '))
qtd_impar=0  #O qtd_impar contabiliza a quantidade de algarismos ímpares
qtd_impar = qtd_impar + numero % 2
i=0 #O i contabiliza a quantidade total de algarismos 

while numero > 0:
    numero= numero // 10
    qtd_impar = qtd_impar + numero % 2
    i=i+1
qtd_pares=i-qtd_impar 
print('Quantidade de dígitos pares: %d' % qtd_pares)
