# functional programming
# lamda()
# lambda is a small anonymouns function that can take any number of arguments,
#  but can only have one experssion
# syntax:  Lambda arguments(s):expression

# example1:
# # UDF
# def greet(name):
#     return "HI," + name


great = lambda name: print("Hi," + name)
# great("Rehan")


# example 2
# def add(x, y):
#     return x + y


add = lambda x, y: x + y
result = add(5, 4)
# print(result)

# map function
# convert string values to intger
str_values = ["4", "5", "9", "2"]
integer_values = []
for value in str_values:
    integer_values.append(int(value))
# print(integer_values)

# using map()
# syntax map(function,*iterable)
# function:built in function,lambda function ,UDF
# print(list(map(int, str_values)))

# for loop is combination of while loop,iterator,next,exception
users = ["ali", "ahmad", "bilal"]
# print(list(map(str.upper, users)))
v1 = [3, 6, 7, 8]
v2 = [2, 6, 8, 1]
v3 = []


# for i in range(len(v1)):
#     v3.append(v1[i] + v2[i])
# print(v3)
def add_values(x, y):
    return x + y


v3 = list(map(add_values, v1, v2))  # map functino using built in UDF
# print(v3)
v1 = [3, 6, 7, 8]
v2 = [2, 6, 8, 1]
v3 = []
v3 = list(map(lambda x, y: x + y, v1, v2))  # map function using lambda function
# print(v3)
# problem
# students = [
#     {"Name": "Ahmad", "age": 24},
#     {"Name": "Riaz", "age": 27},
#     {"Name": "Khalil", "age": 29},
# ]

# # for std in students:
# #     inc = std["age"]
# #     inc += 1
# #     std["age"] = inc


# # print(students)
# # mysolution
# # def increase_age(student):
# #     student["age"] += 1
# #     return student


# # result = list(map(increase_age, students))
# # # print(result)


# # solution 2
# # find adults
# # students = [
# #     {"Name": "Ahmad", "age": 24},
# #     {"Name": "Riaz", "age": 27},
# #     {"Name": "Khalil", "age": 29},
# # ]


# # def increase_age(student):
# #     if student["age"] >= 25:
# #         return student
# #     else:
# #         pass


# # result = list(map(increase_age, students))
# # print(result)
# # ----------------
# # # using filter()
# # students = [
# #     {"Name": "Ahmad", "age": 24},
# #     {"Name": "Riaz", "age": 27},
# #     {"Name": "Khalil", "age": 29},
# #     {"Name": "Mahmod", "age": 17},
# #     {"Name": "tayyab", "age": 29},
# # ]


# # def find_adults(student):
# #     if student["age"] >= 25:
# #         return student["age"]

# #     # else:
# #     #     del student


# # adults_list = list(filter(find_adults, students))
# # print(adults_list)

# data = [{"key1": 10, "key2": 20}, {"key1": 10, "key2": 20}, {"key1": 10, "key2": 20}]


# def add_no(v):
#     for item in data:
#         item["key1"]= item["key1"] + 5
#         item["key2"]= item["key2"] + 5
#         return data


# result = list(map(add_no, data))
# print(result)

jewels = "aA"
stones = "aAAbbb"
occurance = 0
for j in range(len(jewels)):
    if jewels[j] in stones:
        occurance += stones.count(jewels[j])
print(occurance)
