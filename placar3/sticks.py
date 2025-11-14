import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    heaps = list(map(int, input().split()))
    
    soma = 0
    for h in heaps:
        soma ^= h
    
    if soma == 0:
        print("second")
    else:
        print("first")
