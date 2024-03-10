from getpass import getpass

user_name = input("enter username")
password = getpass("enter password")
if user_name == "rehan" and password == "rehan":
    print("welcome")
else:
    print("wrong password")

# i=0
# while i<5:
#     print(i)
#     i+= 1
