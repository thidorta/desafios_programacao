import math

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
        if lista_incial_primos[pos] : lista_final.append(pos)

    return lista_final

def fatora_numero(n: int, lista_crivo: list) -> set:
    lista_fator = set()
    for primo in lista_crivo:
        if primo * primo > n:
            break
        while n%primo == 0:
            n = n//primo
            lista_fator.add(primo)
    if n > 1:                    
        lista_fator.add(n)
    return lista_fator
                    
def totient(n: int, lista_crivo: list) -> int:
    if n == 1:                       
        return 1
    fatorado = fatora_numero(n, lista_crivo)
    resultado = n
    for p in fatorado:
        resultado = resultado // p * (p - 1)
    return resultado

def main():
    qtd = int(input())
    valores_entrada = [int(input()) for _ in range(qtd)]
    crivo_maximo = max(valores_entrada)
    lista_crivo = crivo(crivo_maximo)
    for i in valores_entrada:
        print(totient(i, lista_crivo))
main()