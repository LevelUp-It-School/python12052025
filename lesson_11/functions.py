# def <имя функции>(<аргументы функции>):
#     <тело функции>

# def only_even(numbers):
#     result = True
#     for x in numbers:
#         if x % 2 != 0:
#             result = False
#             break
#     return result

# print(only_even([2, 4, 6]))
# print(only_even([2, 4, 5]))


# def only_even(numbers):
#     for x in numbers:
#         if x % 2 !=0:
#             return False
#     return True

# print(only_even([2, 4, 6]))
# print(only_even([2, 4, 5]))


# print(print("Привет"))

# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True

# print(only_even([2, 4, 6]))
# print(only_even([2, 4, 5]))

# a, b = only_even([2, 4, 5])
# print(a)
# print(b)

# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True

# print(numbers)

# def check_password(pwd):
#     return pwd == password

# password = "Python"
# print(check_password('123'))

# def list_modify():
#     del sample[-1]

# sample = [1, 2, 3]
# list_modify()
# print(sample)

# def list_modify():
#     sample = [4, 5, 6]

# sample = [1, 2, 3]
# list_modify()
# print(sample)

# def summary(x, y):
#     return x+y

# z = summary(10, 15)
# print(z)


# def list_modify_1(list_arg):
#     # создаем новый ловкальный список, не имеющий связи с внешним
#     list_arg = [1, 2, 3, 4]

# def list_modify_2(list_arg):
#     # меняем исходный внешний список, переданный как апргумент
#     list_arg += [4]

# sample_1 = [1, 2, 3]
# sample_2 = [1, 2, 3]

# list_modify_1(sample_1)
# list_modify_2(sample_2)
# print(sample_1)
# print(sample_2)

# def inc():
#     global x
#     x += 1
#     print(f"Количество вызовов функции равно {x}.")

# x = 0
# inc()
# inc()
# inc()

def f(count):
    count += 1
    print(f"Количество вызовов функции равно {count}.")
    return count

count_f = 0
count_f = f(count_f)
count_f = f(count_f)
count_f = f(count_f)
count_f = f(count_f)
