def purchase_item(price: float, player_gold: float) -> float:
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    elif player_gold < price:
        raise ValueError("Insufficient gold")
    else:
        return player_gold - price

def safe_calculate_mana_per_spell(total_mana: int, spell_count: int) -> float:
    try:
        return total_mana / spell_count
    except ZeroDivisionError:
        print(f"Warning: Cannot divide by zero spells.")
        return 0.0

def parse_player_age(age_input: str) -> int:
    try:
        return int(age_input)
    except ValueError:
        raise ValueError(f"Invalid age input: {age_input}. Must be an integer")

def main():
    # Initilizing values
    price = 3.50
    price2 = 7.0
    player_gold = 4.00
    total_mana = 100
    spell_count = 0
    age = "25"
    failed_age = "twentytwo"


    valid_purchase = purchase_item(price, player_gold)

    print("========================================")
    print("    ERROR HANDLING & TYPE HINTS REPORT")
    print("========================================")
    print("--- Test 1: Gold Transactions ---")
    print(f"Purchase successful! Remaing gold: {valid_purchase}")
    try:
          error_purchase = purchase_item(price2, player_gold)
          print(f"Purchase successful! Remaining gold: {error_purchase}")
    except ValueError as e:
        print(e)
    print("--- Test 2: Safe Mana Calculation ---")
    calculate_mana_spell = safe_calculate_mana_per_spell(total_mana, spell_count)
    print(f"Mana per spell ({spell_count} spells): {calculate_mana_spell}")
    convert_age = parse_player_age(age)
    print(f"--- Test 3:  Age Parsing ---")
    print(f"Parsed age: {convert_age} years old")
    try:
        failed_convert_age = parse_player_age(failed_age)
        print(f"Parsed age: {failed_convert_age} years old")
    except ValueError as e:
        print(f"Parsing failed {e}")
    print("========================================")

main()
    