# # python array
# # import array  # built in module for array manipulation

# # v1 = array.array("i", [1, 2, 3, 4, 5])
# # print(v1)
# # v1.insert(2, 6)
# # print(v1)
# # python List vs array
# # 1. list can store different type of data while array store only one type of data
# # 2. list is built in function while array is built in module
# # 3. list is more flexible than array in terms of operations

# # ----------------------
# # Matrix
# # python Dimensions of array and List
# # 0D array                  scalar         (OD tensor according to data science,ML)
# # 1D array                  vector          1D Tensor
# # 2D Numpy array or List    Matrix          2D tensor
# # 3D Numpy array or List    Tensor          3D tensor

# # ------------------------------
# # Python Exception handling
# # 1.syntax error 2. logical error(type error)
# # mechanism control run time errors
# # key components
# # 1. try block,(only  1(mandatory)) -the code that may raise exception
# # except block,(1 or more mandatory) -the code that handle the exception
# # else block, -optional(1 ) the code that handle exception
# # finally block the code that runs regardless of the result


# # def b_sort(sort_arr):
# #     n = len(sort_arr)
# #     for i in range(n):
# #         for j in range(n - i - 1):
# #             if sort_arr[j] > sort_arr[j + 1]:
# #                 sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
# #     return sort_arr


# # try:
# #     values = [9, 6, 8, 2]
# #     sorted_values = b_sort(values)
# # except Exception as err:
# #     print(err)
# # else:
# #     print(sorted_values)
# # finally:
# #     print("Program finally executed")

# # python confrol flow statments
# # pass,break,continue,return, yield

# # pass:-with if statment
# x = 10
# if x > 5:
#     pass
# else:
#     print("x is less than 5")


# # pass with function
# def my_function():
#     pass


# # pass with class
# class myclass:
#     pass


# # 2. break statment
# for i in range(10):
#     if i == 5:
#         print(i)
#         break
#     else:
#         print("loop break")
# # continue statment
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("the loop has been executed")

# # conditional expression || Python ternary operator
# # syntax:[on_true] if [expression] else [on_true]
# marks = 80
# result = ""
# if marks >= 40:
#     result = "pass"
# else:
#     result = "Fail"
# print(result)
# # ternary example
# result = "Pass" if marks >= 40 else "Fail"
# # example 2
# marks = 80
# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"


nums = [1, 2, 3, 4, 6, 8]
res_list = []
i = 1
while i < len(nums):
    for num in nums:
        if i == num:
            i += 1
        else:
            res_list.append(i)
print(res_list)