# sort_arr: list[int] = [0, 10, 6, 9, 4]
# for i in range(len(sort_arr)):
#     for j in range(len(sort_arr) - 1):
#         if sort_arr[j] > sort_arr[j + 1]:
#             sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
# print(sort_arr)


# using function
def b_sort(sort_arr):
    n = len(sort_arr)
    for i in range(n):
        for j in range(n - i - 1):
            if sort_arr[j] > sort_arr[j + 1]:
                sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
    return sort_arr


# Task 2
# message = "rizwan@example.com"
# solution 1:
def extract_info(email):
    username, domain = email.split("@")
    domain, extension = domain.split(".")
    return {"username": username, "domain": domain, "extension": "." + extension}
