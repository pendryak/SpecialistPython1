# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup1 = tuple([random.randint(0, 10) for _ in range(10)])
tup2 = tuple([random.randint(0, 10) for _ in range(15)])
tup3 = tuple([random.randint(0, 10) for _ in range(20)])
tup1 = tuple(set(tup1))
tup2 = tuple(set(tup2))
tup3 = tuple(set(tup3))
print(tup1)
print(tup2)
print(tup3)
count = 0
for elem in tup1:
    if elem in tup2 and elem in tup3:
        count += 1
print(count)
