class Vehicle:
    def __init__(self, the_make, the_model, year):
        self.make = the_make
        self.model = the_model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles


car1 = Vehicle("Honda", "Accord", 2007)
# print(car1.make)
# print(car1.model)
# print(car1.year)
print(car1.mileage)
car1.drive(1000)
print(car1.mileage)


# car2 = Vehicle("Toyota", "Camry", 2016)
# print(car2.make)
# print(car2.model)
# print(car2.year)