# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    for i in range(3):
        sum1 += ticket_number % 10
        ticket_number //= 10
    for i in range(3):
        sum2 += ticket_number % 10
        ticket_number //= 10
    return(sum1 == sum2)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

#во втором тесте считаем, что номер на самом деле 012321, поэтому не является счастливым
