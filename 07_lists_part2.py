def filter_heavy_items(items: list, max_weight: float) -> list:
    # items is a list of tuples.
    filtered_items = []
    for item in items:
        name, weight = item
        if weight <= max_weight:
            filtered_items.append(name)
    
    return filtered_items

def calculate_party_stats(party_levels: tuple) -> tuple:
    min_level = min(party_levels)
    max_level = max(party_levels)
    avg_level = sum(party_levels) / len(party_levels)
    return (min_level, max_level, avg_level)



def main():
    # Initializing values
    items_with_weight = [("Iron Shield", 12.5), ("Horse", 20.0), ("Cow", 15.0)]
    max_weight = 15.0
    party_stats = (10, 25, 18, 40)

    # Calling functions
    list_of_items = filter_heavy_items(items_with_weight, max_weight)
    cal_party_stats = calculate_party_stats(party_stats)


    # Print out the result
    print("====================================")
    print("   ADVANCED LISTS & TUPLES REPORT   ")
    print("====================================")
    print(f"Allowed items: (Max {max_weight} kg): {list_of_items}")
    print(f"Party stats: (Min, Max, Avg): {cal_party_stats}")
    print("====================================")

main()