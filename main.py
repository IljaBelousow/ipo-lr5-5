slovo = input("Введите слово: ")

gласные = set("аоуюыэиеёюя")
soft_hard_signs = set("ьъ")

index = 0

for i in slovo:
    index += 1  
    # Проверяем чем является ли буква 
    if i in gласные or i in soft_hard_signs:
        continue 

    print(i, " - согласный / буква номер - ", index)
