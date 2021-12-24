# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)


path = "files/salaries.txt"
path_out = "files/highly_paid.txt"

f = open(path, "r",encoding='utf-8')
f_out = open(path_out, "w", encoding='utf-8')

lines = f.readlines()
lines = lines[1:]
for line in lines:
    empl = " ".join(line.split()).split()
    empl[3] = float(empl[3])
    if empl[3] > 60000:
        f_out.write(empl[0]+' '+empl[1][0] + '.'+empl[2][0] + '.\n')
