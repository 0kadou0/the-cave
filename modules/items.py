class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name = "Gold",
                         description = "A coin made of gold with {} stamped on one face.".format(str(self.amt)),
                         value = self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
            return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name = "Rock",
                         description = "It's a rock... What more do you need?",
                         value = 0,
                         damage = 5)
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name = "Dagger",
                         description = "Rusty dagger. Better than a rock. Nothing else.",
                         value = 10,
                         damage = 10)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name = "Sword",
                         description = "A sword. It swings and stabs. Pretty basic stuff.",
                         value = 15,
                         damage = 15)
