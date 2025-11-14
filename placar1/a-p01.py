from itertools import combinations

def acha_divisíveis(n: int, k: int, lista_primos):
    soma = 0
    for i in range(1, k+1):
        for combinacao in combinations(lista_primos, i):
            produto_total = 1
            for numero in combinacao:
                produto_total *= numero
                if produto_total > n:
                    break
            if produto_total > n:
                continue
            count = n // produto_total
            if i % 2 == 1:
                soma += count
            else:
                soma -= count
    return soma

def main():
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(acha_divisíveis(n, k, array))

if __name__ == "__main__":
    main()