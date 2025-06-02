# numbers = [10, 20, 30]
# print(numbers)
# print(type(numbers))

# mixed_list = [10, 20.55, 'text']
# print(mixed_list)
# print(type(mixed_list))

# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:3])
# print(numbers[::-1])

# numbers[2] = 50
# print(numbers)

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# print(numbers)

# numbers = []
# for i in range(10):
#     numbers.append(int(input()))
# print(numbers)

# numbers = [10, 20, 30, 40, 50]
# # del numbers[-1]
# # print(numbers)

# del numbers[::2]
# print(numbers)

# x in list_name
# print(1 in [2,3,4,5,1])

# x not in list_name
# print(1 not in [2,3,4])

# s = [1,2]
# t = [3, 40, 50]
# print(s+t)
# print(s*5)
# print(len(t))
# print(min(t))
# print(max(t))
# print(t.index(40))
# print(t.index(0))

# numbers = [1, 1, 1, 2, 3, 5, 1]
# # print(numbers.count(1))
# # print(numbers.clear())
# numbers_2 = numbers.copy()
# # numbers_2 = numbers
# # print(numbers)
# # numbers_2.append('new_element')
# print(id(numbers_2))
# print(id(numbers))

# print(numbers == numbers_2)
# print(numbers is numbers_2)

# a = [1, 2, 3]
# b = a

# print(id(a))
# print(id(b))

# a.append(4)
# print(a)
# print(b)
# print(a == b)
# print(a is b)

# a = [1, 2, 3]
# b = a.copy()

# print(id(a))
# print(id(b))

# a.append(4)
# print(a)
# print(b)
# print(a == b)
# print(a is b)

# a = [[1, 2], [3, 4]]
# b = a.copy()
# b[0].append(999)
# print(a)
# print(b)

# import copy

# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)
# b[0].append(999)
# print(a)
# print(b)

s = [1,2]
t = [3, 4, 5]
# s.extend(t)
# print(s)

# s = [1, 3, 4]
# s.insert(1, "2")
# print(s)


# s = [1, 2, 3]
# x = s.pop(1)
# print(x)
# print(s)

# s = [1, 2, 3, 2, 1]
# s.remove(2)
# print(s)

# s = [1, 2, 3]
# s.reverse() # s = s[::-1]
# print(s)

# s = [2, 3, 1]
# # s.sort(reverse=True)
# # print(s)

# s = sorted(s, reverse=True)
# print(s)
