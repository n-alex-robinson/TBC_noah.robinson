import random

class Character:
    def __init__(self, name="Hero", hitPoints=10, hitChance=50, maxDamage=5, armor=0):
        self._name = name
        self._hitPoints = hitPoints
        self._hitChance = self.hitValues(hitChance, 0, 100, 50)
        self._maxDamage = max(1, maxDamage)
        self._armor = max(0, armor)

    @property
    def name(self):
        return self._name

    @property
    def hitPoints(self):
        return self._hitPoints

    @hitPoints.setter
    def hitPoints(self, value):
        self._hitPoints = value

    @property
    def hitChance(self):
        return self._hitChance

    @property
    def maxDamage(self):
        return self._maxDamage

    @property
    def armor(self):
        return self._armor

    def hitValues(self, value, min = 0, max = 100, default = 0):

        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out

    def printStats(self):
        print(f"{self._name}\n{'=' * 20}")
        print(f"Hit points: {self._hitPoints}")
        print(f"Hit chance: {self._hitChance}")
        print(f"Max damage: {self._maxDamage}")
        print(f"Armor: {self._armor}\n")

    def hit(self, opponent):
        if random.randint(1, 100) <= self._hitChance:
            damage = random.randint(1, self._maxDamage)
            actualDamage = max(0, damage - opponent.armor)
            opponent.hitPoints -= actualDamage
            print(f"{self._name} hits {opponent.name} for {actualDamage} points of damage!")
            print(f"{opponent.name}'s armor absorbs {opponent.armor} points.\n")
        else:
            print(f"{self._name} misses!\n")

def fight(character1, character2):

    while character1.hitPoints > 0 and character2.hitPoints > 0:
        character1.hit(character2)
        print(f"{character1.name}: {character1.hitPoints} HP")
        print(f"{character2.name}: {character2.hitPoints} HP\n")
        
        if character2.hitPoints <= 0:
            print(f"{character1.name} wins!")
            break

        input(f"Press Enter to start {character2.name}'s turn.\n{'=' * 20}")

        character2.hit(character1)
        print(f"{character1.name}: {character1.hitPoints} HP")
        print(f"{character2.name}: {character2.hitPoints} HP\n")
        
        if character1.hitPoints <= 0:
            print(f"{character2.name} wins!")
            break

        input(f"Press Enter to start {character1.name}'s turn.\n{'=' * 20}")