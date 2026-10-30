def find_common_spells(wizard_a: list, wizard_b: list) -> set:
    a_set = set(wizard_a)
    b_set = set(wizard_b)
    spells = a_set & b_set
    return spells

def find_unique_spells(wizard_a: list, wizard_b: list) -> set:
    unique_spells = set()
    for spell in wizard_a:
        if spell not in wizard_b:
            unique_spells.add(spell)
    return unique_spells

def count_total_unique_spells(wizard_a: list, wizard_b: list) -> int:
    return len(set(wizard_a + wizard_b))

def main():
    wizard_1 = ["Fireball", "Heal", "Shield", "Teleport", "Fireball"]
    wizard_2 = ["Heal", "Lightning", "Shield", "Invisibility"]
    common_spells = find_common_spells(wizard_1, wizard_2)
    unique_spells = find_unique_spells(wizard_1, wizard_2)
    total_spells = count_total_unique_spells(wizard_1, wizard_2)
    # Print out the result
    print("====================================")
    print("     SPELLBOOK ANALYSIS REPORT      ")
    print("====================================")
    print(f"Common spells:")
    print("---------------------------------")
    for spell in common_spells:
        print(f"Spell: {spell}")
    print("---------------------------------")
    print(f"Unique spells (Wizard 1 only):")
    print("---------------------------------")
    for spell in unique_spells:        
        print(f"Spell: {spell}")
    print("---------------------------------")
    print(f"Total unique spells: {total_spells}")
    print("====================================")

main()