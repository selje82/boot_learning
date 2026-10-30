def add_item(inventory: dict, item_name: str, count: int) -> dict:
    updated = inventory.copy()
    if item_name in updated:
        updated[item_name] += count
    else:
        updated[item_name] = count

    return updated

def merge_inventories(inv1: dict, inv2: dict) -> dict:
    merged = inv1.copy()
    for key in inv2:
        if key in merged:
            merged[key] += inv2[key]
        else:
            merged[key] = inv2[key]

    return merged

def get_total_item_count(inventory: dict) -> int:
    total = sum(inventory.values())
    
    return total
    

def main():
    player_inv = {"Health potion": 3, "Arrows": 25, "Gold coin": 100}
    added_item = add_item(player_inv, "Arrows", 5)
    chest_loot = {"Gold coin": 50, "Health potion": 2, "Ruby": 1}
    merge = merge_inventories(player_inv, chest_loot)
    total = get_total_item_count(merge)
    # Print out the result
    print("====================================")
    print("       INVENTORY & LOOT REPORT      ")
    print("====================================")
    print(f"Updated inventory:")
    print("---------------------------------")
    for item in added_item:
        amount = added_item[item]
        print(f"Item: {item} | Amount: {amount}")
    print("---------------------------------")
    print(f"Merged inventory:")
    print("---------------------------------")
    for item in merge:
        amount = merge[item]        
        print(f"Item: {item} | Amount: {amount}")
    print("---------------------------------")
    print(f"Total items in bag: {total}")
    print("====================================")

main()
