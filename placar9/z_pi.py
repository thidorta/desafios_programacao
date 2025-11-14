def pi_algorithm (string: str) -> list:
    len_string = len(string)
    
    pi = [0] * len_string
    pi[0] = 0
    j = 0

    for i in range(1, len_string):
        while j > 0 and string[i] != string[j]:
            j = pi[j-1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi

def z_algorithm (string: str) -> list:
    n = len(string)
    if not n:
        return []
    
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i        
            r = i + z[i] - 1 

    return z

def main():
    string = input()
    print(*(z_algorithm(string)))
    print(*(pi_algorithm(string)))

if __name__ == "__main__":
    main()