MIN_LENGTH = 8


def main():
    password = get_password()
    print_password_hidden(password)


def get_password():
    print("Please input a password")
    print("A password is only valid if it has more than {} characters".format(MIN_LENGTH))
    password = input(": ")
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input(": ")
    return password


def print_password_hidden(password):
    print("*" * len(password))


main()
