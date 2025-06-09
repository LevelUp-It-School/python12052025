# countries_and_capitals = [("Россия", "Москва"), ("США", "Вашингтон"), ("Франция", "Париж")]
# for country in countries_and_capitals:
#     if country[0] == "Франция":
#         print(country[1])
#         break

# countries_and_capitals = {"Россия" : "Москва",
#                         "США" : "Вашингтон",
#                         "Франция" : "Париж"}
# print(countries_and_capitals["Франция"])
# countries_and_capitals["Сербия"] = "Белград"
# print(countries_and_capitals)

# d = {"key": "old_value"}
# d['key'] = 'new_value'
# print(d['key'])

# countries_and_capitals = {"Россия" : "Москва",
#                         "США" : "Вашингтон",
#                         "Франция" : "Париж"}

# print(countries_and_capitals['Сербия'])

# countries_and_capitals = {"Россия" : "Москва",
#                         "США" : "Вашингтон",
#                         "Франция" : "Париж"}

# if "Сербия" in countries_and_capitals:
#     print(countries_and_capitals['Сербия'])
# else:
#     print("Страна пока не добавлена в словарь")


# countries_and_capitals = {"Россия" : "Москва",
#                         "США" : "Вашингтон",
#                         "Франция" : "Париж"}

# for country in countries_and_capitals:
#     print(f"У страны {country} столица - {countries_and_capitals[country]}")

# countries = dict()
# country = input()
# str_number = 0
# {
#     Россия: [0, 2, 4]
#     США:  [1, 3]
#     Эквадор: [5, 6] 
# }
# while country != "СТОП":
#     if country not in countries:
#         countries[country] = [str_number]
#     else:
#         countries[country].append(str_number)
#     str_number += 1
#     country = input()

# for country in countries:
#     print(f"{country}: {countries[country]}")

# d = {"a":1, "b": 2, "c": 3}
# print(len(d))

# d = {"a":1, "b": 2, "c": 3}
# del d['a']
# print(d)

# d = {"a":1, "b": 2, "c": 3}
# d.clear()
# print(d)

# d = {"a":1, "b": 2, "c": 3}
# d_new = d.copy()
# print(d_new)

# d = {"a":1, "b": 2, "c": 3}
# print(d.get("e", "Ключа нет")) 

# d = {"a":1, "b": 2, "c": 3}
# for key, value in d.items():
#     print(key, value)

# d = {"a":1, "b": 2, "c": 3}
# for key in d.keys():
#      print(key)

# d = {"a":1, "b": 2, "c": 3}
# for value in d.values():
#      print(value)

# d = {"a":1, "b": 2, "c": 3}
# x = d.pop('a')
# print(x)
# print(d)

countries = dict()
country = input()
str_number = 0

while country != "СТОП":
    countries[country] = countries.get(country, []) + [str_number]
    str_number += 1
    country = input()

for country in countries:
    print(f"{country}: {countries[country]}")


# str_1 = "Ну тут какая то строка"
# d = {"a":[1], "b": [2], "c": [3]}
# # print(d.get("a", []) + [str_1]) 
# print(d['b'])