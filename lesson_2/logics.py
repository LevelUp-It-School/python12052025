# yesterday_temp = int(input("Вчерашняя"))
# today_temp = int(input("Сегодня"))

# if today_temp > yesterday_temp:
#     print("Сегодня теплее, чем вчера")
# elif today_temp < yesterday_temp:
#     print("Сегодня холоднее, чем вчера")
# else:
#     print("Сегодня температура такая же, как вчера.") 

# and, or, not
# ################
# first_letter = input("1 буква ")
# last_letter = input("Последняя буква ")

# if (first_letter == 'а' or first_letter == "А") and (last_letter == 'я' or last_letter == 'Я'):
#     print("Верно")
# else:
#     print("Неверно")
# #################
x = 5
# if x >= 0 and x < 100:
#     pass

# if 0 <= x < 100:
#     pass

# UTF-8

# letter_1 = 't'
# letter_2 = 'w'
# print(letter_1 > letter_2)
# print(ord(letter_1))
# print(ord(letter_2))
# print(chr(116))
# print(chr(119))

# print(ord('W'))

# text = input()
# if 'добр' in text:
#     print("Встретилось 'доброе' слово")
# else:
#     print('Добрых слов для вас нет')

#XOR - ^
# a = True
# b = False

# p = a ^ a
# q = a ^ b
# r = b ^ a
# s = b ^ b

# print(a, 'XOR', a, '=', p)
# print(a, 'XOR', b, '=', q)
# print(b, 'XOR', a, '=', r)
# print(b, 'XOR', b, '=', s)

# print("{0:b}".format(15))

print(15^32)
print(bin(47))
print(bin(15))
print(bin(32))

15 = 001111
32 = 100000
XOR = 101111