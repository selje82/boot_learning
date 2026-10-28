# Calculating XP from level
def calculate_total_xp(level):
    total_xp = 0
    for lvl in range(1, level + 1):
        total_xp += lvl * 100
    return total_xp

# Returing rounds of battle before monster is killed.
def simulate_battle(monster_hp, damage_per_hit):
    rounds = 0
    while monster_hp > 0:
        monster_hp -= damage_per_hit
        rounds += 1
    return rounds

# Counting critical hits
def count_crit_hits(total_attacks):
    crits = 0
    for attack in range(1, total_attacks + 1):
        if attack % 3 != 0:
            continue
        crits += 1
    return crits

def main():
    level = 10
    monster_hp = 100
    damage_per_hit = 25
    attacks = 10
    # Calling functions
    total_xp = calculate_total_xp(level)
    rounds = simulate_battle(monster_hp, damage_per_hit)
    critical_hits = count_crit_hits(attacks)

    # Print out the result. 
    print("=================================")
    print("        LOOPS & BATTLE SIM       ")
    print("=================================")
    print(f"Total XP (Level 1 to {level}): {total_xp}")
    print(f"Rounds to defeat monster ({monster_hp} HP, {damage_per_hit} Dmg): {rounds}")
    print(f"Critical Hits in {attacks} attacks: {critical_hits}")
    print("=================================")

main()




        