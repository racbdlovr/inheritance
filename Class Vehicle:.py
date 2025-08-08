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
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity  # in pounds or kilograms
        self.current_load = 0

    def load_cargo(self, weight):
        if self.current_load + weight <= self.cargo_capacity:
            self.current_load += weight
            print(f"Loaded {weight} units. Current load: {self.current_load}")
        else:
            print(f"Cannot load {weight} units. Overload! Current load: {self.current_load}, Capacity: {self.cargo_capacity}")

    def unload_cargo(self):
        print(f"Unloading all cargo. Previous load: {self.current_load}")
        self.current_load = 0

    def display_info(self):
        super().display_info()
        print(f"Cargo Capacity: {self.cargo_capacity}")
        print(f"Current Load: {self.current_load}")

    def is_overloaded(self):
        return self.current_load > self.cargo_capacity
    
my_truck = Truck("Ford", "F-150", 2022, cargo_capacity=1000)

my_truck.display_info()
my_truck.load_cargo(500)
my_truck.load_cargo(600)  # Should trigger overload warning
print("Is overloaded?", my_truck.is_overloaded())
my_truck.unload_cargo()
my_truck.display_info()

