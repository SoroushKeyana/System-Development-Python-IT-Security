class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine turned off")
 
    
    def fuel_upp(self):
        print("The tank is full!!!")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make,model,year)
        self.num_doors = num_doors
    
    def horn(self):
        print("Honk honk! get out of the way!")

class Bike(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make,model,year)
        self.num_doors = num_gears
    
    def ring(self):
        print("Ringggg! Open the way!")

car1 = Car("Toyota","Corolla","1999", 4)
bike1 = Bike("Honda","GS2343","2020", 15)

print(f"{car1.make} {car1.model} is a very popular car which was manufactured in {car1.year} and has {car1.num_doors} doors.")
car1.start()
car1.horn()
car1.stop()