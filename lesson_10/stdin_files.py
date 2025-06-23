# from sys import stdin

# lines = []
# for line in stdin:
#     lines.append(line.rstrip("\n"))
# print(lines)

# #EOF

# lines = stdin.readlines()
# print(lines)

# text = stdin.read()
# print([text])

# file_in = open('lesson_10\\input_1.txt', encoding="UTF-8")
# for line in file_in:
#     print(line)
# file_in.close()

# with open('lesson_10\\input_1.txt', encoding="UTF-8") as file_in:
#     for line in file_in:
#         print(line.rstrip("\n"))

# with open('lesson_10\\input_1.txt', encoding="UTF-8") as file_in:
#     lines = file_in.readlines()
# print(lines)

# with open('lesson_10\\input_1.txt', encoding="UTF-8") as file_in:
#     symbols = file_in.read(10)
# print([symbols])

# with open('lesson_10\\output_1.txt', 'w', encoding="UTF-8") as file_out:
#     n = file_out.write("Это первая строка\nА это вторая\nИ третья - последняя")
# print(n)

# lines = ["Это первая строка\n", "А это вторая\n", "И третья - последняя"]
# with open('lesson_10\\output_2.txt', 'w', encoding="UTF-8") as file_out:
#     file_out.writelines(lines)

# with open('lesson_10\\output_3.txt', 'w', encoding="UTF-8") as file_out:
#     print("Вывод в файл с помощью функции print()", file=file_out)