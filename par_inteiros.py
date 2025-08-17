from collections import Counter

# recebe uma inteiro n e uma lista de inteiros de tamanho n
# verifica quantos pares de inteiros i,j -> j-i = lista[i] + lista[j]

def verifica_pares(n: int, lista: list) -> int:
    cont = 0
    freq = Counter()
    for i in range(n):
        key = lista[i] + i
        cont += freq.get(i - lista[i], 0)
        freq[key] += 1
    return cont

def main():

    n = int(input())
    lista = list(map(int, input().split()))
    print(verifica_pares(n, lista))

main()