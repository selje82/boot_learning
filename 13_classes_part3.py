class Item:
    def __init__(self, name: str, category: str, value: int):
        self.name = name
        self.category = category
        self.value = value

class Inventory:
    def __init__(self, owner: str):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_items_by_category(self, category: str) -> list[Item]:
        matching_items = []
        for i in self.items:
            if i.category.lower() == category.lower():
                matching_items.append(i)
        return matching_items

    def sell_cheap_items(self, min_value: int) -> None:
        items_to_keep = []
        for i in self.items:
            if i.value >= min_value:
                items_to_keep.append(i)
        self.items = items_to_keep

def main():
    # Initilize some items.
    sword = Item("Iron Sword", "Weapon", 150)
    potion = Item("Health Potion", "Consumable", 20)
    dagger = Item("Poison Dagger", "Weapon", 80)
    bread = Item("Loaf of Bread", "Consumable", 5)

    # Intitlize inventory and add items.
    bag = Inventory("Gimli")
    bag.add_item(sword)
    bag.add_item(potion)
    bag.add_item(dagger)
    bag.add_item(bread)

    # 1. Test category search
    weapons = bag.get_items_by_category("weapon")
    print(f"Weapon in the bag of: {bag.owner}:")
    for w in weapons:
        print(f" - {w.name} (Value: {w.value})")

    # 2. Test to sell cheap items (only keep items worth 50 or more.)
    print("\nSelling things cheaper than 50 gold...")
    bag.sell_cheap_items(50)

    print(f"Items still in the bag: ({len(bag.items)})")
    for item in bag.items:
        print(f" - {item.name}")


if __name__ == "__main__":
    main()