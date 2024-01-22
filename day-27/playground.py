def add(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)

add(1, 2, 4, 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)
