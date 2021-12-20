# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

date = input("date = ")
date_list = date.split(sep='.')
day = int(date_list[0])
month = int(date_list[1])
year = int(date_list[2])

number_list = ["zero","first","second","third","fourth","fifth","sixth","seventh","eighth","ninth"]
teen_list = ["tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth"]
month_list = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
#print("The {0} of {1}, {2}".format)

if day <= 9:
    day_s = number_list[day]
elif 10 <= day <= 19:
    tens = day % 10
    day_s = teen_list[tens]
elif day == 20:
    day_s = "twentieth"
elif day == 30:
    day_s = "thirtieth"
else:
    tens = day % 10
    if day // 10 == 2:
        day_s = "twenty-" + number_list[tens]
    else:
        day_s = "thirty-" + number_list[tens]

print("The {0} of {1}, {2}".format(day_s,month_list[month-1],year))
