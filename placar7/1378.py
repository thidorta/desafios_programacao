def ultimo_digito(n: int) -> int:
    if n == 0:
        return 1
    lista_ultimos_digitos = [8, 4, 2, 6]
    tamanho_lista = len(lista_ultimos_digitos)
    pos = (n-1) % tamanho_lista
    return lista_ultimos_digitos[pos]

def main():
    n = int(input())
    print(ultimo_digito(n))

if __name__ == "__main__":
    main()