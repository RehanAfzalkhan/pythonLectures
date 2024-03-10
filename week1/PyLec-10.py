# # ### list comprehension
# # <p>concise /elegent way of creating a list </p>
# # <p>concise /elegent way of define/creating a list based on the exising lists(existing iterable object)</p>

# # syntax 01:[expression for var iten in iterable]
# # syntax 02: [expression for var iten in iterable if condition ]
# # message = "Python Programming"
# # items = list(message)
# # items.append("!")
# # new_item = "".join(items)
# # print(new_item)

# # message = "Python Programming"
# # new_message = list(message.upper())
# # empt_list = []
# # for var in new_message:
# #     empt_list.append(var * 3)
# # result = "".join(empt_list)
# # print(result)

# # usign list comprehension
# # msg = "Python Programming"
# # items = [(ch * 3).upper() if ch == "P" or ch == "i" else ch.upper() for ch in msg]
# # for ch in msg:
# #     if ch == "P" or ch == "i":
# #         items.append((ch * 3).upper())
# #     else:
# #         items.append(ch.upper())

# # new_msg = "".join(items)
# # print(new_msg)

# # ternary operator || conditional expression
# # [true expression if condition else false expression ]
# # syntax 03: [expression if condition else expression for var in iterable]

# # what is a function:
# # named block of code only run when u call function
# # reuseability
# # modularity
# # maintainability
# # parameters: while defining functions values
# # is the variable listed inside the parenthsis in the function defination.
# # argument :values supply while calling functions
# # return statemnet
# # scope
# # local variable,global variable

# # lamda expressiion
# # problem sort data according to age
# # students = [
# #     {"name": "Ahmad", "age": 24},
# #     {"name": "Bilal", "age": 27},
# #     {"name": "Khalil", "age": 25},
# # ]

# # user defined function (UDF)
# def add_values(x, y):
#     return x + y


# result_values = add_values(5, 10)
# print(result_values)

# # anonymouns function or lamda function
# result_value = lambda a, b: a + b
# print(result_value(15, 20))

# functional programming
# LAMDA
# MAP
# FILTER
# REDUCE

# PARALLEL PROGRAMMING
# ZIP


# async programming
# aysnc, await

# recursive programming
# recursion


# moduler prograamming
# modules,function,classes,global variable,packges

# Object-oriented-programming

# python advanced concept
# 1. decorator
# 2. Iterator
# 3. generator


# 4comprehension
# 5. Generator expresion
# 6. Regex
# user defined function (UDF)
# def add_values(x, y):
#     return x + y


# result_values = add_values(5, 10)
# print(result_values)

# # using lamda
# sum_values = lambda x, y: x + y
# print(sum_values)

# nums = [1, 2, 3, 4, 6, 8]
# res_list = []
# i = 1
# while i < len(nums):
#     for num in nums:
#         if i == num:
#             i += 1
#         else:
#             res_list.append(i)
# print(res_list)
print("helo")
