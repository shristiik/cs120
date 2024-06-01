import tbc

def main():
    hero = tbc.Character(name="Hero", hitPoints=10, hitChance=50, maxDamage=5, armor=2)
    monster = tbc.Character(name="Monster", hitPoints=20, hitChance=30, maxDamage=5, armor=0)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()
