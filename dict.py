# # 1
# def sum_values(dict_):
#     sum_ = 0
#     for value in dict_.values():
#         sum_ += value
#     return sum_
#
#
# dict__ = {"a": 1, "b": 2, "c": 3}
# print(sum_values(dict__))


# # 2
# def reverse_dict(dict_):
#     reversed_dict = {value: key for key, value in dict_.items()}
#     return reversed_dict
#
#
# dict__ = {"a": 1, "b": 2, "c": 3}
# print(reverse_dict(dict__))


# # 3
# def filter_dict(dict_, n):
#     new = {}
#     for key, value in dict_.items():
#         if value > n:
#             new[key] = value
#     return new
#
#
# dict__ = {"a": 1, "b": 2, "c": 3}
# num = int(input("number="))
# print(filter_dict(dict__, num))


# # 4
# def merge_dicts(dict1, dict2):
#     new = {}
#     for d in [dict1, dict2]:
#         for k, v in d.items():
#             if k in new:
#                 new[k] += v
#             else:
#                 new[k] = v
#     return new
#
#
# dict_1 = {"one": 1, "two": 2, "three": 3}
# dict_2 = {"four": 4, "two": 5, "six": 6}
# print(merge_dicts(dict_1, dict_2))


# # 5
# def sort_keys(dict_):
#     new = {}
#     sorted_keys = sorted(dict_.keys())
#     for k in sorted_keys:
#         new[k] = dict_[k]
#     return new
#
#
# dict__ = {"a": 1, "c": 2, "b": 3}
# print(sort_keys(dict__))


# # 6
# def count_values(dict_):
#     new = {}
#     # count = 0
#     for k, v in dict_.items():
#         if v in new:
#             # count += 1
#             new[v] += 1
#         else:
#             # count = 1
#             new[v] = 1
#         # new[v] = count
#     return new
#
#
# dict__ = {"a": 1, "b": 2, "c": 3, "d": 3}
# print(count_values(dict__))


# # 7
# def update_values(dict_, n):
#     new = {k: v*n for k, v in dict_.items()}
#     return new
#
#
# dict__ = {"a": 1, "b": 2, "c": 3}
# num = int(input("num="))
# print(update_values(dict__, num))


# # 8
# def max_key(dict_):
#     list_v = list(dict_.values())
#     max_v = list_v[0]
#     max_k = None
#     for k, v in dict_.items():
#         if v > max_v:
#             max_v = v
#             max_k = k
#     return max_k
#
#
# dict__ = {"a": 1, "b": 4, "c": 3}
# print(max_key(dict__))


# # 9
# def filter_by_key(dict_, keys):
#     new = {}
#     for k, v in dict_.items():
#         if k in keys:
#             new[k] = v
#     return new
#
#
# dict__ = {"a": 1, "b": 4, "c": 3}
# key = {"a", "b", "f"}
# print(filter_by_key(dict__, key))


# # 10
# def combine_dicts(dict1, dict2, dict3):
#     combine = {}
#     for d in [dict1, dict2, dict3]:
#         for k, v in d.items():
#             if k in combine:
#                 combine[k].append(v)
#             else:
#                 combine[k] = [v]
#     return combine
#
#
# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"a": 4, "e": 5, "f": 6}
# dict_3 = {"a": 7, "h": 8, "i": 9}
# print(combine_dicts(dict_1, dict_2, dict_3))