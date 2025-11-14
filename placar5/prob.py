import math
def binomial_probability(n, p):
    q = 1 - p
    total_jogos = 2*n - 1
    total_probabilidade = 0.0
    for i in range(n, total_jogos+1):
        combinacoes = math.comb(i - 1, n - 1)
        prob_i_vitorias = combinacoes * (p ** n) * (q ** (i - n))
        total_probabilidade+=prob_i_vitorias
    return total_probabilidade
def main():
    t = int(input())
    for _ in range(t):
        n_str = input()
        p_str = input()            
        n = int(n_str)
        p = float(p_str)
        probabilidades = binomial_probability(n,p)
        print(f"{probabilidades:.2f}")
main()