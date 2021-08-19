number_tickets = int(input("Введите необходимое количество билетов:"))
s = 0
for price in range (1, number_tickets + 1):
    age = int(input("Введите возраст посетителя:"))
    if 0 <= age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    else:
        price = 1390
if number_tickets>3:
    s = (s + ((price * number_tickets)*0.9))
    print("Общая стоимость ваших билетов:",s)
else:
    s=(s+(price*number_tickets))
    print("Общая стоимость ваших билетов:",s)