# # 1簡單迴圈
# for i in range(1, 11):
#     print(i)

# # 2使用條件判斷的迴圈
# i = 0
# while i < 11:
#     if i % 2 != 0:
#         print(i)
#     i += 1

# # 3巢狀迴圈
# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()

# # 4基本函數定義
# def add_two_numbers(a, b):
#     n = a + b
#     return n
#
#
# x = int(input("number1="))
# y = int(input("number2="))
# print(add_two_numbers(x, y))

# # 5函數與迴圈結合
# def sum_all(n):
#     sum_ = 0
#     for i in range(1, n+1):
#         sum_ += i
#     return sum_
#
#
# num = int(input("number="))
# print(sum_all(num))

# # 6列表理解
# square = [i * i for i in range(1, 11)]
# print(square)

# # **7迴圈與條件判斷的結合
# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# for x in range(2, 101):
#     if is_prime(x):
#         print(f"{x} ", end="")

# # 8函數與條件判斷
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False
#
#
# n = int(input("number="))
# if is_even(n) is True:
#     print("偶數")
# else:
#     print("奇數")

# # 9
# def multiply(a, b):
#     return a * b
#
#
# def add(c, d):
#     return c + d
#
#
# a = int(input("number1="))
# b = int(input("number2="))
# c = multiply(a, b)
# d = int(input("number3="))
# print(add(multiply(a, b), d))

# # 10
# word = input("string=")
# reverse = ""
# for i in range(len(word)-1, -1, -1):
#     reverse += word[i]
# print(reverse)