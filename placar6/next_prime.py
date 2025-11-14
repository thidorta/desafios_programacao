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

def verifica_primo(n: int) -> bool:
    lista_crivo = crivo(n)
    for i in lista_crivo:
        if n % i == 0:
            return False
    return True
        
def atual_proximo(n: int) -> int:
    if verifica_primo(n):
        return n
    if n % 2 == 0:
        n += 1
    while not verifica_primo(n):
        n += 2
    return n

def main():
    n = int(input())
    print(atual_proximo(n))

if __name__ == "__main__":
    main()