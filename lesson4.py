price = int(input("Введите цену: "))
is_vip = str(input("Вы VIP? (да/нет) - ")).lower()
discount = None

if price >= 1000:
    if is_vip == "да":
        discount = 0.25
    else:
        discount = 0.2
elif price >= 500 and price < 1000:
    discount = 0.1
elif price < 500:
    discount = 0
else:
    print("Ошибка!")

print(f"Товар на {price} со скидкой {discount * 100}% будет стоить {price * (1 - discount)}")
# Я знаю что в 17 строке больше чем 80 символов :)
