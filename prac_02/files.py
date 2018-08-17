# name_file = open("name.txt", "w")
# your_name = (input("Enter your name"))
# print(your_name, file=name_file)
# name_file.close()

# your_other_name = open("name.txt", "r")
# print("You're name is", your_other_name.read())
# your_other_name.close()

# numbers = open("numbers.txt", "r")
# first_number = numbers.readline()
# second_number = numbers.readline()
# print(int(first_number) + int(second_number))
# numbers.close()

file_name = open("numbers.txt", "r")
total = 0
for i in file_name:
    number = int(i)
    total += number
print(total)
file_name.close()
