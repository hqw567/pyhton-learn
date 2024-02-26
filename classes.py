class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def move(self):
        print(f"{self.make} {self.model} is moving")


car = Vehicle("Toyota", "Corolla", 2015)
car.move()


class A(Vehicle):
    def move(self):
        print(f"{self.make} {self.model} is moving A")


class B(Vehicle):
    def move(self):
        print(f"{self.make} {self.model} is moving B")


class C(Vehicle):
    pass


a = A("Toyota A", "Corolla", 2015)
b = B("Toyota B", "Corolla", 2015)
c = C("Toyota C", "Corolla", 2015)

for v in [a, b, c]:
    v.move()
