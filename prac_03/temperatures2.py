MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Operate menu"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_fahrenheit_to_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_celsius_to_fahrenheit(fahrenheit)
            print("result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


# TODO ask Lindsay (now with spelling2.0) why the main does so much.
# It looks like the main does menu navigation, input selection and
# returning of results all in one

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    return fahrenheit * 5 / 9 - 32


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


main()
