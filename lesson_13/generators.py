# squares = (i ** 2 for i in range(10))
# print(squares)

# __next__()


def fib(n):
    n_1, n_2 = 1, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2

# print(", ".join(str(x) for x in fib(10)))
f = fib(100000000)
for i in range(7):
    print(next(f))

# def fruit_generator():
#     for item in ['apple', 'banana', 'cherry']:
#         yield item
# fruit = fruit_generator()
# print(next(fruit))
# print(next(fruit))
# print(next(fruit))
