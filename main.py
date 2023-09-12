summa = float(input("Введите сумму вклада: "))
year = int(input("Введите количество лет: "))

s = summa * (1 + 1.8) ** year

print("Сумма на счету через", year,"лет: ", round(s,2),"vice city")