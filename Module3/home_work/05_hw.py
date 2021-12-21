# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
l = 0
res = ''
for name in names:
    if len(name) > l:
        res = name
        l = len(name)
print(res)
