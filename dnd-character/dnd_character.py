from random import randint


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.charisma = self.ability()
        self.wisdom = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolls = [randint(1, 6) for x in range(4)]
        rolls.sort()
        rolls.reverse()
        return sum(rolls[:3])

def modifier(value):
    return (value - 10) // 2