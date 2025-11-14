import math
EPS = 1e-9 
PI = math.pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def to_vec(o: Point, a: Point) -> Point:
    return Point(a.x - o.x, a.y - o.y)

def dot(v1: Point, v2: Point) -> float:
    return v1.x * v2.x + v1.y * v2.y

def norm_sq(v: Point) -> float:
    return v.x**2 + v.y**2

def angle(a: Point, o: Point, b: Point) -> float:
    oa = to_vec(o, a)
    ob = to_vec(o, b)
    dot_product = dot(oa, ob)
    norm_product_sq = norm_sq(oa) * norm_sq(ob)

    if norm_product_sq < EPS:
        return 0.0

    denominator = math.sqrt(norm_product_sq)
    cos_theta = dot_product / denominator
    cos_theta = max(-1.0, min(1.0, cos_theta))

    return math.acos(cos_theta)

def ccw(a: Point, b: Point, c: Point) -> bool:
    return ((b.x - a.x) * (c.y - a.y) - \
          (b.y - a.y) * (c.x - a.x)) > EPS

# feito com base no slides Problemas de Geometria Computacional

def esta_no_poligono(P, lista_pontos):
    tamanho = len(lista_pontos)
    if tamanho == 0:
        return False
    soma = 0
    for i in range(tamanho-1):
        if  ccw(P, lista_pontos[i], lista_pontos[i+1]):
            soma += angle(lista_pontos[i], P, lista_pontos[i+1]) 
        else:
            soma -= angle(lista_pontos[i], P, lista_pontos[i+1])

    return math.fabs(math.fabs(soma) - 2 * PI) < EPS

def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            
            poligono = []
            for _ in range(n):
                linha = input().split()
                x = float(linha[0])
                y = float(linha[1])
                poligono.append(Point(x, y))
                
            poligono.append(poligono[0])
            
            linha_pt = input().split()
            pt_x = float(linha_pt[0])
            pt_y = float(linha_pt[1])
            pt = Point(pt_x, pt_y)
            
            if esta_no_poligono(pt, poligono):
                print("T")
            else:
                print("F")
        except EOFError:
            break
    
if __name__ == "__main__":
    main()