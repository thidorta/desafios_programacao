def lps (string: str) -> list:
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

def encontra_as_bordas(string: str):
    
    len_string = len(string)
    lista_final = []
    pi = lps(string)
    mais_longa = pi[len_string-1]

    while mais_longa > 0:
        lista_final.append(mais_longa)
        mais_longa = pi[mais_longa-1]
    
    return lista_final[::-1]

def main():
    string1 = input()
    print(*(encontra_as_bordas(string1)))

if __name__ == "__main__":
    main()