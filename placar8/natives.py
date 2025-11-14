n = int(input())
treasures = list(map(int, input().split()))

tamanho = len(treasures)
soma = 0
treasures.sort()
meio = tamanho // 2

if tamanho % 2 != 0:
    for treasure in treasures[meio+1:]:
        soma += treasure
else:
    for treasure in treasures[meio:]:
        soma += treasure
print(soma)