numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] - 3
numbers[-1] - 2
numbers[3] - 1
numbers[:-1] - 3,1,4,1,5,9,2
numbers[3:4] - 1
5 in numbers - 9
7 in numbers - IndexError
"3" in numbers - TypeError
numbers + [6, 5, 3] - numbers = 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
"""

numbers[0] = "ten"

numbers[-1] = 1

print(numbers[2:7])

if 9 in numbers:
    print("True")
else:
    print("False")
