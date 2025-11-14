def mdc(a, b):
    while b:
        a, b = b, a % b  
    return a

def acha_qtd_movimentos(N, S, K):
    minimo = mdc(N, K)

    if S % minimo != 0:
        return -1
    else:
        n = N//minimo
        k = K//minimo
        trono_alvo = (N-S) // minimo 
        invK = pow(k, -1, n)
        moves =(trono_alvo*invK) %  n

    return(moves)

def main():
    T = int(input())
    for i in range(T):
        N, S, K = map(int, input().split())
        print(acha_qtd_movimentos(N,S,K))
if __name__ == "__main__":
    main()