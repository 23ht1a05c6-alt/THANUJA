class Vehicle:
    def __init__(self, vehicle_number, owner_name, parking_hours):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.parking_hours = parking_hours

    def calculate_bill(self):
        return 0


class Car(Vehicle):
    def calculate_bill(self):
        return self.parking_hours * 30


class Bike(Vehicle):
    def calculate_bill(self):
        return self.parking_hours * 15


class Truck(Vehicle):
    def calculate_bill(self):
        return self.parking_hours * 50


n = int(input())

vehicles = []
total_revenue = 0
highest_bill = 0
highest_vehicle = None

for i in range(n):
    vehicle_type = input()
    vehicle_number = input()
    owner_name = input()
    parking_hours = int(input())

    if vehicle_type.lower() == "car":
        v = Car(vehicle_number, owner_name, parking_hours)
    elif vehicle_type.lower() == "bike":
        v = Bike(vehicle_number, owner_name, parking_hours)
    elif vehicle_type.lower() == "truck":
        v = Truck(vehicle_number, owner_name, parking_hours)

    vehicles.append(v)

print("\nVehicle Bills:")
for v in vehicles:
    bill = v.calculate_bill()
    total_revenue += bill

    print("Vehicle No:", v.vehicle_number)
    print("Owner:", v.owner_name)
    print("Bill: ₹", bill)
    print()

    if bill > highest_bill:
        highest_bill = bill
        highest_vehicle = v

print("Total Revenue: ₹", total_revenue)
print("Highest Bill Vehicle:", highest_vehicle.vehicle_number)
print("Owner:", highest_vehicle.owner_name)
print("Bill: ₹", highest_bill)
