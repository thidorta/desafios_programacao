import sys
n = int(input())
input = sys.stdin.readline
array = list(map(int, input().split()))

def soma_alternada(lista):
    soma = 0
    sinal = 1  
    for i in lista:
        soma += i * sinal
        sinal *= -1  
    return soma

s = soma_alternada(array)

lista_final = [0]*n
lista_final[0] = s
for j in range(n-1):
    lista_final[j+1] = 2*array[j] - lista_final[j]
    
print(*lista_final)
