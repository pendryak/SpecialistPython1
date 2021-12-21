# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
r1 = float(input("r1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
r2 = float(input("r2 = "))

dist = distance(x1, y1, x2, y2)
min_r = min(r1, r2)
max_r = max(r1, r2)
print(dist + min_r < max_r)
