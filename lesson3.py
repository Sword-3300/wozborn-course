row = "яблоко:2,банан:3,груша:4,апельсин:6,яблоко:2"
output = {}

pairs = row.split(",")

for pair in pairs:
    product, number = pair.split(":")
    if product in output: #Если в словаре уже есть такой продукт
        output[product] += int(number) # Добавить число к существующему числу
    else: # Если в словаре первый раз встречается такой продукт
        output[product] = int(number) # Добавить совершенно новый продукт и его число

print(output)