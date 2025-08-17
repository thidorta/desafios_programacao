# recebemos a string s
# se a string for palíndromo, não da pra alterar nenhum caractere
# se a string não for palíndromo, vamos verificar se alterando um caractere ela vira um palíndromo
# se tem um digito só, da pra alterar o único dígito
# se tem mais de um dígito, vamos verificar cada digito diferente e contar quantos são diferentes

def pode_ser_palindromo(s: str) -> bool:
    n = len(s)
    count = 0
    reversed_s = s[::-1]

    if (s == reversed_s and n%2 == 0) and n > 1:
        print("NO")
        return
    if n == 1:
        print("YES")
        return
    
    # s-> abbc
    #reversed_s -> cbba

    for i in range(n):
        if s[i] != reversed_s[i]:
            count += 1
            
    if count > 2:
        print("NO")
        return
    print("YES")
    return

def main():
    s = input().strip()
    pode_ser_palindromo(s)
main()