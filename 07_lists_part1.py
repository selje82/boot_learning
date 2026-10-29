
def add_and_remove_first(inventory: list, new_item: str) -> list:
    working_list = inventory
    working_list.append(new_item)
    working_list.pop(0)
    return working_list

def get_equipment_slice(items: list, start: int, end: int) -> list:
    return items[start:end]

def check_inventory_capacity(inventory: list, max_capacity: int) -> str:
    if len(inventory) >= max_capacity:
        return "Inventory full"
    else:
        return f"Space remaining: {max_capacity - len(inventory)}"

def main():
    # Initializing values
    starting_gear = ["Sword", "Shield", "Health potion", "Mana potion"]
    extra_item = "Spear"
    max_capacity = 4
    start_value = 2
    end_value = 4

    # Calling functions
    updated_gear = add_and_remove_first(starting_gear, extra_item)
    quick_slots = get_equipment_slice(starting_gear, start_value, end_value)
    check_capacity = check_inventory_capacity(starting_gear, max_capacity)

    # Print out the result. 
    print("=================================")
    print("   INVENTORY MANAGEMENT (PART 1) ")
    print("=================================")
    print(f"Original gear: {starting_gear}")
    print(f"Updated gear: {updated_gear}")
    print(f"Selected Quick-slots (Index {start_value} to {end_value}): {quick_slots}")
    print(f"Capacity status: {check_capacity}")
    print("=================================")

main()