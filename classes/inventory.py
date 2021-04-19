class Item:
    def __init__(self, name, type, dmg, amount, desc):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.amount = amount
        self.desc = desc

    def remove(self, number):
        self.amount -= number

    def add(self, number):
        self.amount += number
