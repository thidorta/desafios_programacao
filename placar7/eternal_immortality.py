import math

def factorial(a: int, b: int) -> int:
    sub = b - a
    if b == 0 or sub == 0:
        return 1
    if sub >= 10:
        return 0
    resposta = b
    while sub != 1:
        resposta = (resposta * (b-1)) % 10
        b -= 1
        sub -= 1
    return resposta

def main():
    a, b = map(int, input().split())
    n = factorial(a, b)
    print(n%10)

if __name__ == "__main__":
    main()
