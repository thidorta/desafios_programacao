import math

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def gcd_fact(a, b):
    return math.factorial(min(a, b))

def main():
    a, b  = (map(int, input().split()))
    print(gcd_fact(a, b))
main()