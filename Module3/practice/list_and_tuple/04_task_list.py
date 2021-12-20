# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
n = int(input("n = "))
numbers = []
for i in range(n):
    numbers.append(random.randint(-10,10))
print(numbers)
sum = 0
for i in numbers:
    if i > 0:
        sum += i
print(sum)
