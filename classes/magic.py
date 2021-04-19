import random


class Spell:
    def __init__(self, name, type, dmg, cost):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.cost = cost

    def generate_spell_damage(self):
        mgl = self.dmg - 25
        mgh = self.dmg + 25
        return random.randrange(mgl, mgh)
