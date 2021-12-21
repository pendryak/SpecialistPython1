# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def format_time(seconds):
    if seconds >= 60*60*100:
        return("Слишком много секунд для заданного формата (больше 100 часов)")
    sec = seconds % 60
    seconds //= 60
    min = seconds % 60
    hour = seconds // 60
    s = str(hour).rjust(2, '0')+':'+str(min).rjust(2, '0')+':'+str(sec).rjust(2, '0')
    return(s)
