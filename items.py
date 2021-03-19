# Class for items inside of the game
class Item():
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

# Stores the attributes for weapons, inherits from the items class
class Weapon(Item):

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\n{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


# Will be starting weapon for the Fighter Class
class Sword(Weapon):

    def __init__(self):
        self.name = 'Short Sword'
        self.description = 'Small, lightweight, one-handed melee weapon'
        self.value = 0
        self.damage = 1

# Will be starting weapon for the Cleric Class
class Mace(Weapon):

    def __init__(self):
        self.name = 'Mace'
        self.description = 'One handed, spiked mace'
        self.value = 0
        self.damage = 1

# Will be starting weapon for the Mage Class
class Wand(Weapon):

    def __init__(self):
        self.name = 'Wand'
        self.description = 'Small, crooked, wodden wand.'
        self.value = 0
        self.damage = 1

# Will be starting weapon for the Ranger Class
class Bow(Weapon):

    def __init__(self):
        self.name = 'Bow'
        self.description = 'Recurve bow'
        self.value = 0
        self.damage = 1


