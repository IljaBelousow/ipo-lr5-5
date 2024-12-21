slovo = input("Введите слово: ")

glasn = set("аоуюыэиеёюя")
razdel = set("ьъ")

index = 0

for i in slovo:
    index += 1  
    # Проверяем чем является ли буква 
    if i in glasn or i in razdel:
        continue 

    print(i, " - согласный / буква номер - ", index)
