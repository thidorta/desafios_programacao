votos = list(map(int, input().split()))
#indice 4 sempre é o total restante
votos_restantes = votos[4]
soma_total = votos[0]+votos[1]+votos[2]+votos[3]+votos[4]
pode_ganhar = list()
#indices fixos
lista_tartarugas = ["Rafael", "Leonardo", "Donatello", "Michelangelo"]
for i in range(len(votos)-1):
    soma_tartaruga = votos_restantes + votos[i]
    if soma_tartaruga > (soma_total/2):
        pode_ganhar.append(lista_tartarugas[i])
pode_ganhar = sorted(pode_ganhar)
if not pode_ganhar:
    print("sem vencedores")
else:
    for tartaruga in pode_ganhar:
        print(tartaruga)