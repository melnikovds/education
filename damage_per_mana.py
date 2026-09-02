spells = [
    ("Огненный шар", 50, 30),
    ("Ледяной осколок", 30, 10),
    ("Молния", 40, 20)
]

print(type(spells[0]))

def damage_per_mana(spell):
    return spell[1] / spell[2]

sorted_spells = sorted(
    spells,
    key=damage_per_mana,
    reverse=True
)

print(sorted_spells)
