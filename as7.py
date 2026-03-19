import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)

cars = []

for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_s = random.randint(150, 200)
    cars.append(Car(reg, max_s))

race_on = True
while race_on:
    for car in cars:

        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_on = False

print("Reg Num    | Max Speed  | Cur Speed  | Distance")
print("-" * 50)
for car in cars:
    print(f"{car.registration_number:10} | {car.max_speed:10} | {car.current_speed:10} | {car.travelled_distance:.1f} km")