class Item():
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    
class Weapon(Item):

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\n{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)



if __name__=="__main__":
    new_item = Weapon('Bolter', 'A high damage pistol', 50, 10)
    print(new_item)