def t1():
        countr = {"Russia": "Moscow", "France": "Paris","Germany" : "Berlin", "Japan" : "Tokyo" }
        for key in countr:
            print([key], ":", countr[key])

        x = input("Страна")
        if x in countr.keys():
            print(countr[x])
        else:
            print("error")
        list_keys = list(countr.keys())
        list_keys.sort()
        for i in list_keys:
            print(i, ":", countr[i])

def t2():

    x = {1: list("АВЕИНОРСТ"), 2: list("ДКЛМПУ"), 3: list("БГЁЬЯ"), 4: list("ЙЫ"), 5: list("ЖЗХЦЧ"),8: list("ШЭЮ"), 10: list("ФЩЪ") }

    word = input("Введите слово: ").upper()

    count = 0

    for i in word:
        for key, value in x.items():
            if i in value:
                count += key
                break
    print(f"Стоимость слова '{word}' составляет {count} очков.")




task = int(input('Введите номер задачи '))
if task == 1:t1()
if task == 2:t2()
