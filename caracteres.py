n = int(input())
string = input().strip() 
count = 0
menor = 0
indice_minimo = 0
for i in range(n-1):
    if string[i] == '(':
        count += 1
    else: #string[i] == ')'
        count -= 1
    if count < menor:
        menor = count
        indice_minimo = i+1
print(indice_minimo%n)
