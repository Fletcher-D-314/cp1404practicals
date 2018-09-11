from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar_added = Guitar(name, year, cost)
    guitars.append(guitar_added)
    print(guitar_added, "added.")
    name = input("Name: ")

guitars.sort()
print("These are my guitars: ")
position = 0
for guitar in guitars:
    position += 1
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(position, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
