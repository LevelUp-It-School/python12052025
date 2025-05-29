# 1. Построить треугольник, где строки содержат цифры от 1 до номера строки
# 1
# 12
# 123
# 1234
# 12345
# Итерируемся от 1 до N
# Внутри от 1 до i+1
# Печатать внутренний цикл j print(j, end="")
# for i in range(1, 12):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("")

# 2. Вывести квадрат из # размером 4х4
# for i in range(4):
#     for j in range(4):
#         print("#", end="")
#     print("")

#3. Построить треугольник, начиная с 5 звездочек.    
# *****  
# ****  
# ***  
# **  
# *  
# brick = "*"
# size = 5
# while size > 0:
#     print(brick * size)
#     size -= 1

# brick = "*"
# size = 5
# for i in range(size, 0, -1):
#     for _ in range(i):
#         print(brick, end="")
#     print("")
4.

#######
#     #
#     #
#     #
#######
# for row in range(5):
#     for col in range(7):
#         if row==0 or row==4 or col==0 or col==6:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()