# This is a sample Python script.
# 11.1

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name, end ="")


class Book(Publication):
    def __init__(self, name, author, page_nr):
        super().__init__(name)
        self.author = author
        self.page_nr = page_nr

    def print_information(self):
        super().print_information()
        print("Author " + self.author + ":" + str(self.page_nr) + " pages" )


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        super().print_information()
        print("Chief editor: " + self.editor)


pubs = []
pubs.append(Magazine("Donald Duck", "Aki Hyyppä"))
pubs.append(Book("Compartment No. 6", "Rosa Liksom" , 192))

for pub in pubs:
    pub.print_information()


# 11.2
##from Excercise9 import Car( to import car class from exercise 9)
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed =0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed=0
        self.travelled_distance=0

    def accelerate(self,change_speed):
        self.current_speed += change_speed
        if self.current_speed >= self.maximum_speed:
            self.current_speed= self.maximum_speed
        elif self.current_speed <= 0:
            self.current_speed = 0

    def drive(self,number_hours):
        self.travelled_distance += self.current_speed*number_hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery):
        super().__init__(registration_number,maximum_speed)
        self.battery = battery


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank):
        super().__init__(registration_number, maximum_speed)
        self.tank = tank


elec_car = ElectricCar("ABC-15", 180, 52.5)
gaso_car = GasolineCar("ACD-123", 165, 32.3)

gaso_car.accelerate(120)
elec_car.accelerate(100)

gaso_car.drive(3)
elec_car.drive(3)

print(gaso_car.travelled_distance)
print(elec_car.travelled_distance)



