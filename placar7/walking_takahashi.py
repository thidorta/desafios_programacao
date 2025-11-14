X, K, D = map(int, input().split())

X = abs(X)

numero_minimo_passos = X // D

if numero_minimo_passos > K:
    numero = X - D*K
else:
    pos = X % D
    restantes = K - numero_minimo_passos
    if restantes % 2 == 0:
        numero = pos
    else:
        numero  = min(abs(pos - D), abs(pos + D))
    
print(numero)