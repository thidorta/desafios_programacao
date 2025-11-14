import sys
def alinhamento_string(P: str, Q: str) -> int:

    n = len(P)
    m = len(Q)

    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1): 
        table[i][0] = i
    for j in range(1, m+1):
        table[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if P[i-1] == Q[j-1]:
                custo = table[i - 1][j - 1]    
            else:
                custo = table[i - 1][j - 1] + 1 
        
            custo_deletar = table[i-1][j] + 1
            custo_inserir = table[i][j-1] + 1
            table[i][j] = min(custo, custo_deletar, custo_inserir)
      
    return(table[n][m])

def main():

    data = []
    while True:
        try:
            linha1 = sys.stdin.readline().strip()
            if not linha1:
                break
            parte1 = linha1.split(maxsplit=1)
            if len(parte1) < 2:
                break
            string_x = parte1[1]
            linha2 = sys.stdin.readline().strip()
            if not linha2:
                break
            parte2 = linha2.split(maxsplit=1)
            if len(parte2) < 2:
                break
            string_y = parte2[1]

            data.append((string_x, string_y))
        except:
            break
    
    for x,y in data:
        resultado = alinhamento_string(x, y)
        print(resultado)

if __name__ == "__main__":
    main()