# print(";".join(str(1/x) for x in range(int(input()), int(input())+1)))


# interval = range(int(input()), int(input())+1)
# if 0 in interval:
#     print("Диапазон содержит 0.")
# else:
#     print(";".join(str(1/x) for x in interval))
          

# start = input()
# end = input()

# if not (start.lstrip("-").isdigit() and end.lstrip("-").isdigit()):
#     print("Необходимо ввести два числа")
# else:
#     interval = range(int(start), int(end)+1)
#     if 0 in interval:
#         print("Диапазон содержит 0.")
#     else:
#         print(";".join(str(1/x) for x in interval))


# try:
#     <код, который может вызыввать исключения>
# except <КлассИсключения_1>:
#     <обработка ошибки этого типа>
# except <КлассИсключения_2>:
#     <обработка ошибки другого типа>
# ...
# else:
#     <выполняется, если исключений не было>
# finally:
#     <выполняется всегда -- и при ошибках, и без>

# except Exception

# ПРАВИЛЬНО ТАК!!!!!
# try:
#     print(1 / int(input()))
# except ZeroDivisionError:
#     print("Ошибка деления на ноль")
# except ValueError:
#     print("Невозможно преобразовать строку в число")
# except Exception:
#     print("Неизвестная ошибка")

# А ТАК НЕПРАВИЛЬНО!!!!!!112
# try:
#     print(1 / int(input()))
# except Exception:
#     print("Неизвестная ошибка")
# except ZeroDivisionError:
#     print("Ошибка деления на ноль")
# except ValueError:
#     print("Невозможно преобразовать строку в число")

# try:
#     print(1 / int(input()))
# except ZeroDivisionError:
#     print("Ошибка деления на ноль")
# except ValueError:
#     print("Невозможно преобразовать строку в число")
# except Exception:
#     print("Неизвестная ошибка")
# else:
#     print("Операция выполнена успешно!")
# finally:
#     print("Программа завершена")

# try: 
#     print(";".join(str(1/x) for x in range(int(input()), int(input())+1)))
# except ValueError:
#     print("Необходимо ввести 2 числа")
# except ZeroDivisionError:
#     print("Диапазон содержит ноль")

# raise <КлассИсключения>(сообщение)

# x = int(input())
# if x<0:
#     raise ValueError("Число должно быть положителным")

# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
# +-- StopIteration
# +-- StopAsyncIteration
# +-- ArithmeticError
# | +-- FloatingPointError
# | +-- OverflowError
# | +-- ZeroDivisionError
# +-- AssertionError
# +-- AttributeError
# +-- BufferError
# +-- EOFError
# +-- ImportError
# | +-- ModuleNotFoundError
# +-- LookupError
# | +-- IndexError
# | +-- KeyError
# +-- MemoryError
# +-- NameError
# | +-- UnboundLocalError
# +-- OSError
# | +-- BlockingIOError
# | +-- ChildProcessError
# | +-- ConnectionError
# | | +-- BrokenPipeError
# | | +-- ConnectionAbortedError
# | | +-- ConnectionRefusedError
# | | +-- ConnectionResetError
# | +-- FileExistsError
# | +-- FileNotFoundError
# | +-- InterruptedError
# | +-- IsADirectoryError
# | +-- NotADirectoryError
# | +-- PermissionError
# | +-- ProcessLookupError
# | +-- TimeoutError
# +-- ReferenceError
# +-- RuntimeError
# | +-- NotImplementedError
# | +-- RecursionError
# +-- SyntaxError
# | +-- IndentationError
# | +-- TabError
# +-- SystemError
# +-- TypeError
# +-- ValueError
# | +-- UnicodeError
# | +-- UnicodeDecodeError
# | +-- UnicodeEncodeError
# | +-- UnicodeTranslateError
# +-- Warning
# +-- DeprecationWarning
# +-- PendingDeprecationWarning
# +-- RuntimeWarning
# +-- SyntaxWarning
# +-- UserWarning
# +-- FutureWarning
# +-- ImportWarning
# +-- UnicodeWarning
# +-- BytesWarning
# +-- EncodingWarning
# +-- ResourceWarning

# class NumbersError(Exception):
#     pass

# class EvenError(NumbersError):
#     pass

# class NegativeError(NumbersError):
#     pass

# def no_even(numbers):
#     if all(x % 2 != 0 for x in numbers):
#         return True
#     raise EvenError("В списке не должно быть четных чисел")

# def no_negative(numbers):
#     if all(x >= 0 for x in numbers):
#         return True
#     raise NegativeError("В списке не должно быть отрицательных чисел")

# def main():
#     print("Введите числа в одну строку через пробел")
#     try:
#         numbers = [int(x) for x in input().split()]
#         if no_negative(numbers) and no_even(numbers):
#             print(f"Сумма чисел равна: {sum(numbers)}")
#     except NumbersError as e:
#         print(f"Произошла ошибка: {e}")
#     except Exception as e:
#         print(f"Произошла непредвиденная ошибка: {e}")

# if __name__ == "__main__":
#     main()


# if __name__ == "__main__":
#     main()

# import example_module

# example_module.some_function()


# from example_module import some_function, ExampleClass

# some_function()