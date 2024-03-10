# problem 1 vector addition
# v1 = [1, 2, 3]
# v2 = [2, 3, 5]

# solution 1
# v3=[]
# i=0
# for v in v1:
#     v3.append(v+v2[i])
#     i+=1
# print(v3)

# solution 2 range function
# v3=[]
# i=0
# for i in range(len(v1)):
#     v3.append(v1[i]+v2[i])
#     i+=1
# print(v3)

# solution 3 using enumerate function
# v3 = []

# for i,v in enumerate(v1):
#     v3.append(v+v2[i])

# print(v3)


# flatten array
# convert 2D list to 1D list
# mat = [[2, 5, 1], [5, 6, 7]]
# # solution 1 nested if
# vector = []
# for v in mat:
#     vector.extend(v)

# print(vector)


# Nested list
# nested If-else statement
# Nested Loop statments

# Dict
# matrix =2*3
# mat = []
# for i in range(2):
#     vector = []
#     for j in range(3):
#         vector.append(j)
#     mat.append(vector)
# print(mat)

# problem
# matrix = [[2, 4, 6], [1, 2, 4], [3, 7, 1], [2, 7, 1]]  # rows:4,col:3

# # result = [[2, 1, 3, 2], [4, 2, 7, 7], [6, 4, 1, 1]] rows:3,col:4
# transpose_mat = []
# for i in range(len(matrix[0])):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_mat.append(transpose_row)
# print(transpose_mat)

# --------------------------
# list comprehension(list+for+if_clause)
# syntax1: [expression for var in iterable]
# users = ["ahmad", "bilal", "anas", "khalil"]
# new_users = []

# for user in users:
#     new_users.append(user.title())
# print(new_users)

# using list comprehension solution 1
# new_users = [user.title() for user in users]
# print(new_users)
# syntax1: [expression for var in iterable if condition]
users = ["ahmad", "bilal", "anas", "khalil"]

# solution
new_users = []
for user in users:
    if len(user) > 4:
        new_users.append(user)

print(new_users)
# sollutuion with list comprehension
new_users = [user for user in users if len(user) > 4]
print(new_users)


# ternary operator---conditional statement
matrix = [[2, 5, 1], [3, 8, 4]]
vector = []

# -------------------
# 4 march assigment using functions
# 1. bubble sort
# 2. rehan@example.com ---find #domain using for loop using a function
#  output
# a.username=   rehan
# b.domain=     example
# c.            .com

# exception handling
