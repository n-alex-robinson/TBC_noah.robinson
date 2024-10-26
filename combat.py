import tbc

def main():
    hero = tbc.Character(name="Hero", hitPoints=10, hitChance=50, maxDamage=5, armor=2)
    monster = tbc.Character(name="Monster", hitPoints=20, hitChance=30, maxDamage=5, armor=0)

    print("Character Stats:\n")
    hero.printStats()
    monster.printStats()

    print(f"{'=' * 20}\nCombat Begins!\n")
    tbc.fight(hero, monster)

main()