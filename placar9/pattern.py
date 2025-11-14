def find_pattern(texto: str, pattern: str) -> int:
    len_texto = len(texto)
    len_pattern = len(pattern)
    lps = [0] * len_pattern

    lps = preprocess(pattern, len_pattern, lps)

    i = j = count = 0

    while(i < len_texto):
        if pattern[j] == texto[i]:
            j += 1
            i += 1
        if j == len_pattern:
            count += 1
            j = lps[j - 1]
        elif (i<len_texto and pattern[j] != texto[i]):
            if j!=0:
                j = lps[j-1]
            else:
                i += 1
    return count

def preprocess(pattern: str, len_pattern: int, lps: list) -> list:
    tamanho = 0
    lps[0] = 0

    i = 1

    while(i < len_pattern):
        if (pattern[i] == pattern[tamanho]):
            tamanho += 1
            lps[i] = tamanho
            i += 1
        else:
            if (tamanho != 0):
                tamanho = lps[tamanho - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def main():

    string1 = input()
    string2 = input()

    print(find_pattern(string1, string2))

if __name__ == "__main__":
    main()