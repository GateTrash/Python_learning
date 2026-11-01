# - Найди все уникальные записи о покупках. +
# - Найди товары, которые покупали оба человека. +
# - Найди товары, которые покупал только первый человек. +
# - Найди товары, которые покупал только второй человек. +
# Важно: для сравнения товаров используй названия, а не целые кортежи, потому что количество одного и того же товара может различаться.
buy_1 = (
    ("bread", 2),
    ("milk", 1),
    ("apple", 5),
    ("bread", 2)
)
buy_2 = (
    ("milk", 1),
    ("cheese", 3),
    ("apple", 5),
    ("juice", 2)
)
producs_1 = []
producs_2 = []

for item in buy_1:
    if item[0] not in producs_1: producs_1.append(item[0])
print(f"person 1: {producs_1}")

for item in buy_2:
    if item[0] not in producs_2: producs_2.append(item[0])
print(f"person 2: {producs_2}")

unique_products = []
identical_products = []
person_1 = []
person_2 = []
for item_1 in producs_1:
    if item_1 in producs_2: identical_products.append(item_1)
    if item_1 not in producs_2 : 
        unique_products.append(item_1)
        person_1.append(item_1)
for item_2 in producs_2:
    if item_2 not in producs_1 : 
        unique_products.append(item_2)
        person_2.append(item_2)

print(f"identical products: {identical_products}")
print(f"unique products: {unique_products}")
print(f"products buy only 1 person: {person_1}")
print(f"products buy only 2 person: {person_2}")