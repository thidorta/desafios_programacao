import math

LIMITE_DA_RAIZ = 1000001

def crivo(n: int) -> list:
    lista_final = list()
    if n < 2:                   
        return lista_final
    lista_incial_primos = [True for _ in range(n)]
    lista_incial_primos[0] = lista_incial_primos[1] = False
    raiz = math.isqrt(n)     
    for i in range(2, raiz+1):
        if lista_incial_primos[i]:
            for p in range(i*i, n, i):
                lista_incial_primos[p] = False
        continue
    for pos in range(len(lista_incial_primos)) :
        if lista_incial_primos[pos] : lista_final.append(pos*pos)
    return lista_final

def busca_binaria(lista_crivo_raizes: list, n: int) -> bool:
    fim = len(lista_crivo_raizes) - 1
    inicio = 0
    while inicio <= fim:
        meio = (inicio+fim) // 2
        if lista_crivo_raizes[meio] == n:
            return True
        if n > lista_crivo_raizes[meio]:
            inicio = meio+1
        else:
            fim = meio-1
    return False

def main():
    lista_limite_crivo = crivo(LIMITE_DA_RAIZ) 
    n = int(input())
    lista = list(map(int, input().split()))
    for i in lista:
        if busca_binaria(lista_limite_crivo, i):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()