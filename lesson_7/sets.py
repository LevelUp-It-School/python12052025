# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# print(vowels)
# print(type(vowels))
# empty_set = set()
# print(f"Длина пустого множества равна {len(empty_set)}.")

# word = "коллекция"
# letters = set(word)
# print(letters)

# animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра", "страус", "крокодил"]
# print(set(animals))

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# letter = input("Введите букву русского алфавита: ")
# if letter.lower() in vowels:
#     print("Гласная буква")
# else:
#     print("Согласная буква")

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# for letter in vowels:
#     print(letter)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_union = s_1.union(s_2) # s_1 | s_2
# print(s_union)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_intersection = s_1.intersection(s_2) # s_1 & s_2
# print(s_intersection)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_dif = s_1.difference(s_2) # s_1 - s_2
# print(s_dif)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_sym_dif = s_1.symmetric_difference(s_2) # s_1 ^ s_2
# print(s_sym_dif)

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# letters = set("коллекция")
# print(", ".join(letters & vowels))

# s_1 = {1, 2, 3}
# s_2 = {3, 1, 2, 2}
# print(s_1 == s_2)

# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 <= s_2)

# s_1 = {1, 2, 3, 4}
# s_2 = {1, 2, 3}
# print(s_1 >= s_2)

# s = set()
# s.add(1)
# print(s)

# s = set()
# s.add(1)
# print(s)

# s = {1, 2, 3}
# s.remove(2)
# print(s)

# s = {1, 2, 3}
# s.discard(1)
# print(s)

# s = {'dog', 2, 3, 4, "cat"}
# x = s.pop()
# print(x)
# print(s)

s = {1, 2, 3}
s.clear()
print(s)