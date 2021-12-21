# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
n = int(input("n = "))
numbers = [random.randint(-100, 100) for _ in range(n)]
print(numbers)
print(sum(x for x in numbers if x > 0 and x % 2))
