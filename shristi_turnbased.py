# tbc.py
import random

class Character:
    def __init__(self, name, hitPoints, hitChance, maxDamage, armor):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = self.testInt(hitChance, 0, 100, hitChance)
        self.maxDamage = self.testInt(maxDamage, 1, maxDamage, maxDamage)
        self.armor = self.testInt(armor, 0, armor, armor)

    def testInt(self, value, min, max, default):
        if isinstance(value, int) and min <= value <= max:
            return value
        else:
            print(f"Invalid value: {value}. Setting to default: {default}")
            return default

    def printStats(self):
        print(f"{self.name}\n"
              f"==================\n"
              f"Hit points: {self.hitPoints}\n"
              f"Hit chance: {self.hitChance}\n"
              f"Max damage: {self.maxDamage}\n"
              f"Armor: {self.armor}\n")

    def hit(self, opponent):
        randomNumber = random.randint(1, 100)
        if randomNumber <= self.hitChance:
            damage = random.randint(1, self.maxDamage)
            absorbed = min(damage, opponent.armor)
            actual_damage = damage - absorbed
            opponent.hitPoints -= actual_damage
            print(f"{self.name} hits {opponent.name} for {actual_damage} points of damage "
                  f"(absorbed {absorbed} points)\n")
        else:
            print(f"{self.name} misses {opponent.name}\n")

def fight(character1, character2):
    character1.printStats()
    character2.printStats()
    
    round_count = 0
    while character1.hitPoints > 0 and character2.hitPoints > 0:
        round_count += 1
        input(f"Press Enter for round {round_count}: ")
        
        print(f"Round {round_count}:\n")
        
        character1.hit(character2)
        if character2.hitPoints <= 0:
            print(f"{character2.name} has been defeated! {character1.name} wins!")
            break

        character2.hit(character1)
        if character1.hitPoints <= 0:
            print(f"{character1.name} has been defeated! {character2.name} wins!")
            break
        
        print(f"{character1.name}: {character1.hitPoints} HP\n"
              f"{character2.name}: {character2.hitPoints} HP\n")

# combat.py
import tbc

def main():
    hero = tbc.Character(name="Hero", hitPoints=10, hitChance=50, maxDamage=5, armor=2)
    monster = tbc.Character(name="Monster", hitPoints=20, hitChance=30, maxDamage=5, armor=0)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()
