"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
while not finished:
    try:
        number = int(input("Please enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", number)

# TODO - ask Lindsey why his version (below) has the result = 0

# finished = False
# result = 0
# while not finished:
#     try:
#         result = int(input("Enter a valid integer: "))
#         finished = True
#     except ValueError:
#         print("Please enter a valid integer.")
# print("Valid result is:", result)
