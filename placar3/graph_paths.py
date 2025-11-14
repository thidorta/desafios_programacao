MOD = 1000000007

def multiplicar_matrizes(a, b):
    tamanho = len(a)
    c = [[0]*tamanho for _ in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            for k in range(tamanho):    
                c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % MOD
    return c

def exponenciacao(matriz, n):
    tamanho = len(matriz)
    identidade = [[0] * tamanho for _ in range(tamanho)]
    for i in range(tamanho):
        identidade[i][i] = 1
    
    if n == 0:
        return identidade
    
    if n % 2 == 0:
        temp = exponenciacao(matriz, n//2)
        return multiplicar_matrizes(temp, temp)
    
    temp = exponenciacao(matriz, n-1)
    return multiplicar_matrizes(matriz, temp)

def main():
    n, m, k = map(int, input().split())
    matriz_adjacente = [[0] * n for _ in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        matriz_adjacente[x-1][y-1] += 1
    
    resultado = exponenciacao(matriz_adjacente,k)
    print(resultado[0][n-1]%MOD)


if __name__ == "__main__":
    main()