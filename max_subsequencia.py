qtd_dias = int(input())
dias = list(map(int, input().split()))

maior_sequencia_atual = list()
count = 1
first_day = 0
last_day = 0

for i in range(len(dias)-1):
    if dias[i+1] == dias[i]+1:
        count += 1
        last_day = dias[i+1]
    else:
        maior_sequencia_atual.append(count)
        count = 1
        first_day = dias[i+1]
        
maior_sequencia_atual.append(count)
print(max(maior_sequencia_atual))