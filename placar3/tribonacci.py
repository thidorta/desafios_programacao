MOD = 1000000009

def multiplicar_matrizes(a, b):
    c = [[0]*len(a) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):    
                c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % MOD
    return c

def exponenciacao(matriz, n):
    identidade = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
    
    if n == 0:
        return identidade
    
    if n % 2 == 0:
        temp = exponenciacao(matriz, n//2)
        return multiplicar_matrizes(temp, temp)
    
    temp = exponenciacao(matriz, n-1)
    return multiplicar_matrizes(matriz, temp)

def tribonacci(n):
    #casos base
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    matriz = [[1,1,1],
              [1,0,0],
              [0,1,0]]
    
    resultado = exponenciacao(matriz, n-3)

    return (resultado[0][0] * 2 + resultado[0][1] * 1 + resultado[0][2] * 0) % MOD

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(tribonacci(n))
if __name__ == "__main__":
    main()