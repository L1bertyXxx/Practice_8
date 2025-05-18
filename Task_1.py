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