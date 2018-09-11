YEAR = 2018
VINTAGE = 50


class Guitar:
    """Guitar class for storing details of a guitar"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string of a guitar's details"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE

    def get_age(self):
        """Retrieves the age of a guitar"""
        return YEAR - self.year

    def is_vintage(self):
        """Determines if a guitar is vintage"""
        if self.get_age() >= VINTAGE:
            return True
        else:
            return False
