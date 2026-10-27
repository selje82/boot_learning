# Character
player_name = "Kyabrin"
level = 1
health_percent = 100.0
is_alive = True

# Experience (XP)
current_xp = 1100
quest_reward_xp = 450
# New XP after quest is done
total_xp = current_xp + quest_reward_xp

print("=================================")
print("     CHARACTER STATUS REPORT     ")
print("=================================")
print(f"Player: {player_name} | Level: {level}")
print(f"Health: {health_percent} | Alive: {is_alive}")
print("---------------------------------")
# Setting starting gold for character
gold = 100
print(f"Starting Gold: {gold}")
# Cost for potion
potion_cost = 40
print(f"Bought 2 potions for {potion_cost * 2}")
# Updating gold amount after potions is bought
gold -= (potion_cost * 2)
print(f"Remaining Gold: {gold}")
print("---------------------------------")
print(f"Current XP: {current_xp}")
print(f"Gained XP after doing quest: {quest_reward_xp}")
print(f"New XP after quest: {total_xp}")
print("=================================")
