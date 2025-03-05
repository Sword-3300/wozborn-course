herbs = int(input("Сколько трав добавить: "))
crystals = int(input("Сколько кристалов добавить: "))
water = int(input("Сколько воды добавить: "))
firedust = int(input("Сколько огненной пыли добавить: "))
moonlight = int(input("Сколько лунного света добавить: "))

ingridients = herbs + crystals + water + firedust + moonlight
magic_power = herbs * 0.5 + crystals * 1.5 + water * 0.8 + firedust + moonlight * 1.2

magic_power += ((ingridients > 150) * 20)

print("Магическая сила зелья: ", magic_power)