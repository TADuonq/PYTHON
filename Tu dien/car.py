class Car:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year
    
    def get_full_name(self):
        return f"Full name car is: {self.brand}{self.name}"