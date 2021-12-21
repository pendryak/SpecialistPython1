# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    if n == 1 or n == 2:
        return(1)
    f_0 = 1
    f_1 = 1
    f = 0
    for i in range(n-2):
        f = f_0 + f_1
        f_0 = f_1
        f_1 = f
    return(f)
