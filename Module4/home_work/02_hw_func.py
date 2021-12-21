# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


xa = float(input("xa = "))
ya = float(input("ya = "))
xb = float(input("xb = "))
yb = float(input("yb = "))
xc = float(input("xc = "))
yc = float(input("yc = "))

ab = distance(xa, ya, xb, yb)
ac = distance(xa, ya, xc, yc)
bc = distance(xc, yc, xb, yb)

dist = {"AB": ab, "AC": ac, "BC": bc}
min_line = min(dist.values())
line = [k for k, v in dist.items() if v == min_line]
print("Самый короткий отрезок:", line[0])  # Выводим название отрезка, например “АС”.
