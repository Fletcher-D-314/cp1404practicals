total_price = 0
number_of_items = int(input("Enter quantity of items: "))
while number_of_items <= 0:
    print("Invalid number")
    number_of_items = int(input("Enter quantity of items: "))
for i in range(number_of_items):
    item_price = float(input("Enter price of item"))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.9
print("Total price for ", number_of_items, "items is: $", total_price)
