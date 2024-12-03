slovo = str(input("vvedite slovo "))
index = 0
for i in slovo:#проходит по slovo
    index += 1
    if i == "а" or i == "о" or i == "у" or i == "ы" or i == "э" or i == "и" or i == "е" or i == "ё" or i == "ю" or i == "я":#выводит ничего
        print("")
    elif i == "ь" or i =="ъ":#выводит ничего
        print("")
    else:#иначе выводит согласную юукву и её номер
        print(i, " - согласный / буква номер - ", index)
