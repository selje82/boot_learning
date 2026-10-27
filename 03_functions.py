def calculate_damage(base_damage, multiplier):
    return base_damage * multiplier

def format_health(current_hp, max_hp):
    return f"{current_hp}/{max_hp} HP"

def calculate_score(xp, gold):
    return (xp + (gold * 2))

damage = calculate_damage(10, 2)
health = format_health(20, 100)
score = calculate_score(100, 20)

print("=================================")
print("       QUEST BATTLE REPORT       ")
print("=================================")
print(f"Damage dealt: {damage}")
print(f"Player health: {health}")
print(f"Total score: {score}")
print("=================================")