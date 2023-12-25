# # 1列表逆序
# def reverse(list_):
#     reversed_ = []
#     for i in range(len(list_)-1, -1, -1):
#         reversed_.append(list_[i])
#     return reversed_
#
#
# list_ = [1, 2, 3]
# print(reverse(list_))

# # 2找出最大數
# def max_num(list_):
#     i = 1
#     max_ = list_[0]
#     while i < len(list_):
#         if list_[i] > max_:
#             max_ = list_[i]
#         i += 1
#     return max_
#
#
# list_ = [1, 2, 3]
# print(max_num(list_))


# # 3計算列表中正數的數量
# def positive(list_):
#     positive_ = 0
#     for i in list_:
#         if i > 0:
#             positive_ += 1
#     return positive_
#
#
# list_ = [-1, 2, -4]
# print(positive(list_))


# # 4
# def combine(list1, list2):
#     # combine_ = []
#     # for i in list1:
#     #     combine_.append(i)
#     # for j in list2:
#     #     combine_.append(j)
#     # return combine_
#     combine_ = list1 + list2
#     return combine_
#
#
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(combine(list_1, list_2))


# # 5
# def slicing(list_, index_start, index_end):
#     return list_[index_start:index_end+1:]
#
#
# list__ = [1, 2, 4, 5]
# start = 1
# end = 2
# print(slicing(list__, start, end))


# # 6
# def diagonal(list_):
#     element = []
#     for i in range(len(list_)):
#         for j in range(len(list_)):
#             if i == j:
#                 element.append(list_[i][j])
#     return element
#
#
# list__ = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(diagonal(list__))


# # 7
# def check(list_, element):
#     for i in list_:
#         if i == element:
#             return True
#     return False
#
#
# list__ = [1, 3, 4, 5]
# e = 6
# print(check(list__, e))


# # 8
# def distinct(list_):
#     new = []
#     for i in list_:
#         if i not in new:
#             new.append(i)
#     return new
#
#
# list__ = [1, 1, 2, 3, 4, 4]
# print(distinct(list__))


# # 9
# def sum_(list_):
#     sum_int = 0
#     for i in list_:
#         if isinstance(i, int):
#             sum_int += i
#     return sum_int
#
#
# list__ = [1, 2, 3, ""]
# print(sum_(list__))

# # 10
# def min_even(list_):
#     even = []
#     for i in list_:
#         if i % 2 == 0:
#             even.append(i)
#     j = 1
#     min_e = even[0]
#     while j < len(even):
#         if even[j] < min_e:
#             min_e = even[j]
#         j += 1
#     return min_e
#
#
# list__ = [1, 2, 3, 4, 5]
# print(min_even(list__))

# # 11
# def square(list_):
#     new = []
#     for i in list_:
#         new.append(i*i)
#     return new
#
#
# list__ = [1, 3, 4, 5, 6]
# print(square(list__))


# # 12
# def mix(list1, list2):
#     mix_ = []
#     i = 0
#     while i < len(list1) or i < len(list2):
#         if i < len(list1):
#             mix_.append(list1[i])
#         if i < len(list2):
#             mix_.append(list2[i])
#         i += 1
#     return mix_
#
#
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(mix(list_1, list_2))


# # 13
# def len_str(list_):
#     length = []
#     for i in list_:
#         if isinstance(i, str):
#             length.append((i, len(i)))
#     return length
#
#
# list__ = ["a", "as", "asdf", 3]
# print(len_str(list__))


# # 14
# def sort(list_):
#     for i in range(1, len(list_)):
#         if list_[i-1] > list_[i]:
#             return False
#     return True
#
#
# list__ = [1, 2, 5, 4]
# print(sort(list__))


# # 15
# def spin(list_, n):
#     if len(list_) == 0 or n % len(list_) == 0:
#         return list_
#     n = n % len(list_)
#     rotate = list_[-n:] + list_[:-n]
#     return rotate
#
#
# list__ = [1, 2, 3, 4]
# num = int(input("number="))
# print(spin(list__, num))





