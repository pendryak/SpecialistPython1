# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def perimeter(l1,l2,l3):
    return(l1+l2+l3)

def square(l1,l2,l3):
    p = perimeter(l1,l2,l3)/2
    return(math.sqrt(p*(p-l1)*(p-l2)*(p-l3)))


xa = float(input("xa = "))
ya = float(input("ya = "))
xb = float(input("xb = "))
yb = float(input("yb = "))
xc = float(input("xc = "))
yc = float(input("yc = "))

l1 = dist(xa,ya,xb,yb)
l2 = dist(xa,ya,xc,yc)
l3 = dist(xc,yc,xb,yb)

p = perimeter(l1,l2,l3)
s = square(l1,l2,l3)

if s == 0:
    print("Точки не образуют треугольник")
else:
    print("Периметр:", p)
    print("Площадь:", s)

# Не забудьте протестировать вашу функцию
