n = int(input())
bits = int(input())
valores = list(map(int, input().split()))
valores = sorted(valores)

soma_total = sum(valores)

if (soma_total > bits-1) or (soma_total < -bits):
    print("N")
else:
    print("S")
    print(*valores, sep=" ")