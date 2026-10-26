# Character settings
character = "Kyabrin"
role = "Mage"
level = 1
server = "EU1"

# Status and XP
xp = 100
xp_for_quest = 50
new_xp = xp + xp_for_quest
status = "Ready for next quest"

# Printing out information about character and status
print("===============================")
print("     TERMINAL QUEST SYSTEM     ")
print("===============================")
print(f"Character: {character}")
print(f"Role: {role}")
print(f"Level: {level}")
print(f"Server: {server}")
print(f"Current XP: {xp}")
print(f"Quest XP: {xp_for_quest}")
print(f"XP after completed quest: {new_xp}")
print(f"Status: {status}")
print("===============================")

