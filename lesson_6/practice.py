# 1. text = "Hello world"
# Найдите первую заглавную букву в строке, если ее нет, то выведите сообщение, что нет.
# text = "hello world"
# found = False
# for char in text:
#     if char.isupper():
#         print(f'Первая заглавная буква {char}')
#         found = True
#         break
# if not found:
#     print("Нет заглавных букв")

# 2. text = "!!!Hello!!! world!!!"
# Удалить все !!! только в конце строки, но не в середине.
# text = "!!!Hello!!! world!!!"
# # while len(text)>0 and text[-1]=="!":
# #     text = text[:-1]
# # print(text)
# while text.endswith('!'):
#     text = text[:-1]
# print(text)

#3. text = "Python 3.13 is awesome in 2025"
# Удаление чисел из строки

# text = "Python 3.13 is awesome in 2025"
# result = ''
# for char in text:
#     if not char.isdigit():
#         result += char
# print(result)

# 4. text = "Hello world 23232 1321 brother"
# посдчет гласных и согласных
# vowels = 'aeiouy'
# text = "HEllo world 23232 1321 brother"
# vowels = 'aeiouy'

# vowels_counter = 0
# consonant_counter = 0
# for char in text:
#     if char.isalpha():
#         if char.lower() in vowels:
#             vowels_counter += 1
#         else:
#             consonant_counter += 1

# print(f"Согласных = {consonant_counter}, гласных = {vowels_counter}")

# 5. text = "This is a simple Python string example"
#  Пропустить слова с длиной < 5
# text = "This is a simple Python string example"
# words = text.split()

# for word in words:
#     if len(word) > 4:
#         print(word)

# 6. У вас есть список животных. Посчитайте сколько раз каждое животное встречается.
animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра"]

# Уникальные животные = ["слон", "тигр", "зебра"]
# Счетчик = [1, 1, 1]

# 1. Проитерироваться по списку Animals
# 2. Проверять если нет животного в уникальных животных и если нет то добавляем
# 3. В список счетчика добавляем 1
# 4. ЕСЛИ животное не уникально: Получить индекс этого животного в списке уникальных
# 5. Из списка счетчика получить счетчик с индексом из П.4 и +=1

animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра", "страус", "крокодил"]
unique_animals = []
counts = []

for animal in animals:
    if animal not in unique_animals:
        unique_animals.append(animal)
        counts.append(1)
    else:
        index = unique_animals.index(animal)
        counts[index] += 1

for i in range(len(unique_animals)):
    print(f"{unique_animals[i]}: {counts[i]}")