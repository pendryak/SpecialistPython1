# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
staff.sort(key=operator.itemgetter('salary'))
print("Имя и Фамилию сотрудника с самой высокой зарплатой:",staff[-1]['name'],staff[-1]['surname'])

print("Имя и Фамилию сотрудника с самой низкой зарплатой:",staff[0]['name'],staff[0]['surname'])

sal = sum([d["salary"] for d in staff])
print("Среднеарифметическую зарплату всех сотрудников: ",sal/len(staff))

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
for empl in staff:
    print("{0} {1}".format(empl['name'],empl['surname']))


staff.sort(key=operator.itemgetter('surname'))
count = 0
c = 0
surname = staff[0]['surname']
for i in range(1,len(staff)):
    if staff[i]['surname'] == surname:
        c += 1
    else:
        surname = staff[i]['surname']
        if c != 0:
            count += c + 1
            c = 0
if c != 0:
    count += c + 1

print("Количество однофамильцев в организации:",count)
