import ninja

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)
        return self


my_treats = ["snausage", "Bacon", "Trash Bag"]
my_pet_food = ["pizza", "Burger"]

Buddy = Pet("Buddy", "dog", ["Buddy on things", "is invisible"], "Woof")

John = ninja.Ninja("John", "Doe", Buddy, my_treats, my_pet_food)

John.feed()
John.feed()
John.feed()
