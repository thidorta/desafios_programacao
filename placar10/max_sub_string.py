import sys

def max_sub_string(P: str, Q: str) -> int:

    n = len(P)
    m = len(Q)

    table = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if P[i-1] == Q[j-1]:
                table[i][j] = table[i-1][j-1] + 1    
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
        
    return(table[n][m])

def main():
    while True:
        try:
            line1 = sys.stdin.readline().strip()
            if not line1:
                break
            line2 = sys.stdin.readline().strip()
            result = max_sub_string(line1, line2)
            print(result)
        except EOFError:
            break
        except Exception as e:
            break
if __name__ == "__main__":
    main()