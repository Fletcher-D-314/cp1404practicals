"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print(limo.odometer)
    print(limo)

main()