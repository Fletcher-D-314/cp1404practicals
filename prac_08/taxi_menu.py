from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.car import Car

MENU = "q)uit, c)hoose, d)rive"


def main():
    total_fare = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    taxi_to_drive = None
    while choice != "Q":
        if choice == "C":
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_number = int(input("Choose taxi: "))
            taxi_to_drive = taxis[taxi_number]
            print("Bill to date: ${:.2f}".format(total_fare))
        elif choice == "D":
            if taxi_to_drive is None:
                taxi_to_drive = taxis[0]
            taxi_to_drive.start_fare()
            distance = int(input("Drive how far? "))
            taxi_to_drive.drive(distance)
            bill = taxi_to_drive.get_fare()
            total_fare += bill
            print("Your {} trip will cost you ${:.2f}".format(taxi_to_drive.name, taxi_to_drive.get_fare()))
            print("Bill to date: ${:.2f}".format(total_fare))
        else:
            print("Try again")

        print(MENU)
        choice = input(">>>").upper()
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
