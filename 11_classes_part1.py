class Hero:
    health: int = 40

    def heal(self, amount: int) -> None:
        self.health += amount

def main():
    hero = Hero()
    hero.heal(25)
    print(hero.health)

main()