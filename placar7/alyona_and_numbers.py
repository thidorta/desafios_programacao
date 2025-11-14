import sys
line = sys.stdin.readline().split()
n = int(line[0])
m = int(line[1])
x_dict = dict()
y_dict = dict()

for resto_x in range(5): # todos os restos possíveis ao dividir por 5
    x_dict[resto_x] = (n+5-resto_x) // 5
x_dict[0] = n // 5

for resto_y in range(5):
    y_dict[resto_y] = (m + 5 - resto_y) // 5
y_dict[0] = m // 5

print(x_dict[0] * y_dict[0] + x_dict[1] * y_dict[4] + x_dict[2] *
       y_dict[3] + x_dict[3] * y_dict[2] + x_dict[4] * y_dict[1])

