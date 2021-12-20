# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

# Пример строки перевертыша: "И темен город. Мороз узором дорог не мети."

# TODO: your code here
text = "И темен город. Мороз узором дорог не мети."
s = "".join(c for c in text if c.isalpha()).lower()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
