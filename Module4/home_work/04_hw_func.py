# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def make_val(val_list):
    value = [0, 0, 1]
    if len(val_list) == 1:
        value[0] = val_list[0]
    elif len(val_list) == 2:
        value[1] = val_list[0]
        value[2] = val_list[1]
    else:
        value = val_list
        if val_list[0] < 0:
            value[1] = -value[1]
    return value[0] * value[2] + value[1], value[2]


expr = '-2/3 - -2'
expr = expr.replace('/', ' ')
expr = expr.split()

val1 = []
val2 = []
sign = 1  # 1 - '+', -1 - '-'
num = 1
for i in expr:
    if i != '-' and i != '+' and num == 1:
        val1.append(int(i))
    elif i == '-':
        sign = -1
        num = 2
    elif i == '+':
        num = 2
    else:
        val2.append(int(i))

x1, y1 = make_val(val1)
x2, y2 = make_val(val2)

x3 = x1 * y2 + sign * x2 * y1
y3 = y1 * y2

n = x3 // y3
x = x3 % y3 // math.gcd(x3 % y3, y3)
y = y3 // math.gcd(x3 % y3, y3)

print("{0} {1}/{2}".format(n, x, y))


