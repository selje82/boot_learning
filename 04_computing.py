# Setting intial values
total_gold = 137
party_size = 4

# Definision to divide gold on party size
def divide_gold(gold, party_nr):
    return gold // party_nr

# Definition to find the remaining gold after deviding. 
def remaining_gold(gold, party_nr):
    return gold % party_nr

# Calling devide and remaining function.
gold_per_person = divide_gold(total_gold, party_size)
tips_to_house = remaining_gold(total_gold, party_size)

# Function to calculate spell damage, 
# based on level and power base.
def calculate_spell_damage(level, power_base):
    return power_base ** level

# Calling function to calculate damage.
base = 4
level = 3
damage = calculate_spell_damage(level, base)

# Value for max HP
max_hp = 100
# Initial value for HP after healing
calculated_hp = 115.678
# Capping and rounding value to max HP
capped_hp = round(min(calculated_hp, max_hp),ndigits=1)

# Print out the result. 
print("=================================")
print("     COMPUTING & LOOT REPORT     ")
print("=================================")
print(f"Total gold: {total_gold} | Party size: {party_size}")
print(f"Gold per person: {gold_per_person}")
print(f"Gold remaining (tip): {tips_to_house}")
print("---------------------------------")
print(f"Spell damage (Base {base}, Level {level}): {damage}")
print("---------------------------------")
print(f"Calculated HP: {calculated_hp}")
print(f"Capped & Rounded HP: {capped_hp} / {max_hp}")
print("=================================")
