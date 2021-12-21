# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
{
        "name": "Футболка",
        "brand": "puma",
        "price": 4800
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")
brands = set(item['brand'] for item in items)
print(*brands, sep=', ')

print("На складе больше всего товаров брэнда(ов): ")

brands_dict = {}
for brand in brands:
    brands_dict[brand] = 0


for item in items:
    brands_dict[item['brand']] += 1
max_brands = max(brands_dict.values())

for key,value in brands_dict.items():
    if value == max_brands:
        print(key)


print("На складе самый дорогой товар брэнда(ов): ")
items.sort(key=operator.itemgetter('price'))
max_price_item = len(items)-1
max_price = items[-1]['price']
i = -1
while True:
    if items[i]['price'] == max_price:
        print(items[i]['brand'])
        i -= 1
    else:
        break
