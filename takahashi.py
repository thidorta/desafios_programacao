def takahashi(n: int, m: int, a: list, b: list) -> list:
    for i in range(m):
        aux = b[i] 
        if aux in a:
            a.remove(aux)
    return ' '.join(map(str, a))

def main():
    n, m  = (map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    resultado = takahashi(n, m, a, b)
    print(resultado)
main()