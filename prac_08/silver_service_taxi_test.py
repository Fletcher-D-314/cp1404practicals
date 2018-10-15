from prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=3)
print(hummer)

gocart = SilverServiceTaxi(name="Gocart", fuel=300, fanciness=2)
gocart.drive(18)
print(gocart.get_fare())
