from prac_06.guitar import Guitar
gibson = Guitar("Gibson L-5 CES",1922, 16035.4)
pearl = Guitar("Pearl 7-Piece DK", 2018, 800)
print("{} get_age() - expected 96. Got {}".format(gibson.name, gibson.get_age()))
print("{} get_age() - expected 0. Got {}".format(pearl.name, pearl.get_age()))
print("{} is_vintage() - expected True. Got {}".format(gibson.name, gibson.is_vintage()))
print("{} is_vintage() - expected False. Got {}".format(pearl.name, pearl.is_vintage()))
