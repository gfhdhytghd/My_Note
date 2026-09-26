class Bakery:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def take_order(self):
        print("taking order")

    def chef(self):
        print("cooking")


Waiter1 = Bakery("a", 22)
Waiter2 = Bakery("b", 23)
Waiter3 = Bakery("c", 24)

for waiter in (Waiter1, Waiter2, Waiter3):
    print(waiter.name, waiter.age)
    waiter.take_order()

Waiter1.chef()