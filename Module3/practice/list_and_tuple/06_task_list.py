# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
a = min(first_number,second_number)
b = max(first_number,second_number)
l = []
if a % 3 == 0:
    l.append(a)
elif (a + 1) % 3 == 0 and a + 1 <= b:
    a += 1
    l.append(a)
elif a + 2 <= b:
    a += 2
    l.append(a)
a += 3
while a <= b:
    l.append(a)
    a += 3
print(l)
