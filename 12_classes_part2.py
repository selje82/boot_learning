class Wizard:
    mana: int = 100

    def cast_spell(self, cost: int) -> None:
        self.mana -= cost

def main():
    gandalf = Wizard()
    gandalf.cast_spell(30)

    print(gandalf.mana)

main()