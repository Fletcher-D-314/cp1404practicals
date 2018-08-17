MIN_LENGTH = 8

print("Please input a password")
print("A password is only valid if it has more than {} characters".format(MIN_LENGTH))
password = input(": ")
while len(password) < MIN_LENGTH:
    print("Invalid password")
    password = input(": ")
print("*" * len(password))