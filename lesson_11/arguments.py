# def final_price(price, discount):
#     return price - price * discount / 100

# print(final_price(1000, 5))

# def final_price(price, discount=1):
#     return price - price * discount / 100

# print(final_price(1000, 5))

# print(final_price(1000))

# def add_value(x, list_arg = []):
#     list_arg += [x]
#     return list_arg

# print(add_value(0)) # создался пустой список
# print(add_value(0, [1, 2, 3]))
# print(add_value(1)) # +
# print(add_value(1)) # +
# print(add_value(1)) # +
# print(add_value(1, [1, 2, 3]))

# def add_value(x, list_arg = None):
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]
#     return list_arg


# print(add_value(0)) # создался пустой список
# print(add_value(0, [1, 2, 3]))
# print(add_value(1)) # создался пустой список
# print(add_value(1)) # создался пустой список
# print(add_value(1)) # создался пустой список
# print(add_value(1, [1, 2, 3])) 

# def final_price(price, discount=1):
#     return price - price * discount / 100

# print(final_price(1000, discount=5))
# print(final_price(discount=15, price=1000))


# def final_price(*prices, discount=1): #*args
#     print(prices)
#     return [price - price * discount / 100 for price in prices]

# print(final_price(1000, 500, 450, 124, 2432342342, 44534, discount=5))

# **kwargs

# def final_price(*prices, discount=1, **kwargs):
#     low = kwargs.get('price_low', min(prices))
#     high = kwargs.get('price_high', max(prices))
#     return [price - price * discount / 100 for price in prices if low <= price <= high]

# print(final_price(100, 200, 300, 400, 500, discount=5))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_high=200))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200, price_high=350))

# def only_pos(x):
#     return x > 0

# result = filter(only_pos, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# result = filter(str.isalpha, '12345ABCDefgh$()$@@')
# print("".join(result))

# def square(x):
#     return x ** 2

# map(<функция обработчик>, <итерируемый объект>)
# result = map(square, range(5)) # [0, 1, 2, 3, 4]
# print(", ".join(str(x) for x in result))

# result = map(str.lower, ["abCDF", 'EFGh', 'IJkl'])
# print('\n'.join(result))

# numbers = list(map(int, input().split()))
# print(numbers)

# "1 2 43 6 3".split() -> ["1","2", "43", "6", "3"]

# lambda <аргумент>: <тело функции>

# lambda x: x > 0

# def only_pos(x):
#     return x > 0

# result = filter(lambda x: x > 0, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# def square(x):
#     return x ** 2

# result = map(lambda x: x ** 2, range(5)) # [0, 1, 2, 3, 4]
# print(", ".join(str(x) for x in result))

# lines = ['abcd', 'АБ', 'abc', 'abcdef']
# print(sorted(lines, key=lambda line: len(line)))

# lines = ['abcd',  'abc', 'abcdef', 'ba', 'ab']
# print(sorted(lines, key=lambda line: (-len(line), line)))

# lines = ['abcd',  'abc', 'ba', 'ab', 'acde']
# print(min(lines, key=lambda line: (-len(line), line)))

# result = (x for x in [-1, 5, 6, -10, 0] if x > 0)
# print(", ".join(str(x) for x in result))

# from functools import reduce

# numbers = range(1, 6)
# print(reduce(lambda x, y: x + y, numbers))