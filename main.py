#Jacob Douglas
#main.py (case study)
# this program is to take infroamtion from the user and store into classes of difernt autombiles and super call of vehicle.
# Takes input and stores into data type of which is stored into the cuper class called car then call the function to build a car and print the inputed results. 
class Vehicle: 
  def __init__(self, vehicle_type):
   self.vehicle_type = vehicle_type

class Automobile(Vehicle):
  def __init__(self, vehicle_type, year, make, model, doors, roof): 
    super().__init__(vehicle_type)
    self.year = year
    self.make = make
    self.model = model
    self.doors = doors
    self.roof = roof

def build_car():
  vehicle_type = 'car'
  year = input("Enter the year of the Vehicle: ")
  make = input("Enter the make of the Vehicle: ")
  model = input("Enter the model of the Vehicle: ")
  doors = input("Enter the number of doors (2 or 4): ")
  roof = input("Enter the type of roof (solid, sun roof, or soft top): ")
  car = Automobile(vehicle_type, year, make, model, doors, roof)
  return car
def print_car(car):
  print("Vehicle type:", car.vehicle_type)
  print("Year:", car.year)
  print("Make:", car.make)
  print("Model:", car.model)
  print("Number of doors:", car.doors)
  print("Type of roof:", car.roof)

car = build_car()
print_car(car)
