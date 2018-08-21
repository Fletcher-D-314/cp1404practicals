# numbers = []
#
# for i in range(5):
#     number = int(input("Please input a number: "))
#     numbers.append(number)
# print("Number: {}".format(numbers[0]))
# print("Number: {}".format(numbers[1]))
# print("Number: {}".format(numbers[2]))
# print("Number: {}".format(numbers[3]))
# print("Number: {}".format(numbers[4]))
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is {:.2f}".format(sum(numbers) / 5))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Enter username: ")

if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")

