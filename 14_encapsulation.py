class Player:
    def __init__(self, name: str, initial_gold: int):
        self.__name = name
        self.__gold = initial_gold

    def get_name(self) -> str:
        return self.__name

    def get_gold(self) -> int:
        return self.__gold

    def receive_gold(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__gold += amount

    def pay_player(self, target: "Player", amount: int) -> None:
        if amount <= 0:
            raise ValueError("Cannot pay zero or negative gold")
        elif amount > self.__gold:
            raise ValueError(f"{self.__name} has insufficient gold")
        else:
            self.__gold -= amount
            target.receive_gold(amount)

def main():
    player1 = Player("Gimli", 100)
    player2 = Player("Legolas", 50)

    print(f"{player1.get_name()} har {player1.get_gold()} gold.")
    print(f"{player2.get_name()} har {player2.get_gold()} gold.")

    # 1. Test correct amount
    print("\nGimli betaler Legolas 30 gold...")
    player1.pay_player(player2, 30)

    print(f"{player1.get_name()} har nå {player1.get_gold()} gold.")  # Skal være 70
    print(f"{player2.get_name()} har nå {player2.get_gold()} gold.")  # Skal være 80

    # 2. Test short of gold (should cast ValueError)
    try:
        print("\nGimli prøver å betale Legolas 200 gold...")
        player1.pay_player(player2, 200)
    except ValueError as e:
        print(f"Expected error: {e}")

    # 3. Test negative gold (should cast ValueError)
    try:
        print("\nLegolas tries to pay Gimli -10 gold...")
        player2.pay_player(player1, -10)
    except ValueError as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    main()