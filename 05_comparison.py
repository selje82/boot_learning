# Function to check level and if the player has a key.
def can_enter_dungeon(player_level, has_key):
    return player_level >= 10 and has_key

# Function to check player's health and mana
def get_combat_status(health, mana):
    if health <= 0:
        return "Defeated"
    elif health < 30 or mana < 10:
        return "Critical condition"
    else:
        return "Ready for battle"

# Check VIP status and discount status
def calculate_discount(is_vip, purchase_amount):
    if is_vip or purchase_amount >= 500:
        return 20
    elif purchase_amount >= 200:
        return 10
    else:
        return 0

# Initial values
player_level = 10
has_key = True
is_vip = True
health = 20
mana = 40
purchase_amount = 220

enter_dungeon = can_enter_dungeon(player_level, has_key)
combat_status = get_combat_status(health, mana)
discount = calculate_discount(is_vip, purchase_amount)

# Print out the result. 
print("=================================")
print("    GATEKEEPER & COMBAT SYSTEM   ")
print("=================================")
print(f"Dungeon entry allowed: {enter_dungeon}")
print(f"Combat status: {combat_status}")
print(f"Shop discount rate: {discount}%")
print("=================================")