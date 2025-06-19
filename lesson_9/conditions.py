# [x for x in seq if condition] - фильтрует элементы
# [A if condition else B for x in seq] - выбирает значение по условию

# lst = [x**2 for x in range(11) if x % 2 == 0]
# print(lst)

# lst = ['even' if x % 2 == 0 else "odd" for x in range(1, 11)]
# print(lst)

# lst = ['pass' if x >= 50 else "fail" for x in [70, 40, 55, 50, 90, 100]]
# print(lst)

# lst = [x if x > 0 else 0 for x in [3, 5, 0, -10, -2, 34, 5, -11]]
# print(lst)

scores = [70, 40, 55, 50, 90, 100]
grades = [5 if x >= 90 else
          4 if x >= 70 else
          3 if x >= 55 else
          2 
          for x in scores
          ]
print(grades)