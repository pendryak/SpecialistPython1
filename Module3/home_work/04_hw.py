# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

n = int(input("n = "))
numbers = [random.randint(-100, 100) for _ in range(n)]
#numbers = [2, -5, 8, 9, -25, 25, 4]
print(numbers)
squares = []
for number in numbers:
    if number >= 0:
        square = int(math.sqrt(number))
        if number == square**2:
            squares.append(square)
print(squares)
