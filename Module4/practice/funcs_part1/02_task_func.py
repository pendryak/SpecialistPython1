# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    n = number
    digits = 0
    while n:
        n //= 10
        digits += 1
    digits -= 1
    n = number
    while n:
        if n // (10**digits) != n % 10:
            return False
        n %= 10**digits
        n //= 10
        digits -= 2
    return True

#второй вариант 

def palindrome2(number):
    n = number
    m = 0
    while n:
        m = m * 10 + n % 10
        n //= 10
    return m == number

# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
