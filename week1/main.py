import task as tk

values = [0, 10, 6, 9, 4]
res = tk.b_sort(values)
print(res)


email = input("Enter your email address: ")
info = tk.extract_info(email)
print("Username:", info["username"])
print("Domain:", info["domain"])
print("Extension:", info["extension"])
