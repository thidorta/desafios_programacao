def window(n: int, k: int, lista: list) -> str:
    if k <= 0 or n == 0 or k > n:
        return ""

    freq = {}
    lista_final = []

    # primeira janela
    for x in lista[:k]:
        freq[x] = freq.get(x, 0) + 1
    lista_final.append(len(freq))

    # deslizar janelas usando índices
    for i in range(k, n):
        out_elem = lista[i - k]    # sai
        freq[out_elem] -= 1
        if freq[out_elem] == 0:
            del freq[out_elem]

        in_elem = lista[i]         # entra
        freq[in_elem] = freq.get(in_elem, 0) + 1

        lista_final.append(len(freq))

    return " ".join(map(str, lista_final))


def main():
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(window(n, k, array))

if __name__ == "__main__":
    main()