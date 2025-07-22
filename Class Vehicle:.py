class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def honk(self):
        print("beep beep!")

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


my_car = Car("Honda", "Civic", 2022, 4)
my_car.display_info()
my_car.honk()

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, current_load, unload_cargo, is_overloaded):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.current_load = current_load
        self.unload_cargo = unload_cargo
        self.is_overloaded = is_overloaded
    
    def