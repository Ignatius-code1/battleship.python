
# Character data
characters = {
    '1': {'name': 'Wizard', 'hp': 70, 'damage': 150},
    '2': {'name': 'Elf', 'hp': 100, 'damage': 100},
    '3': {'name': 'Human', 'hp': 150, 'damage': 20}
}

# Dragon stats
dragon_hp = 300
dragon_damage = 50

# Character selection
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    choice = input("Choose your character (1-3): ")
    
    if choice in characters:
        character = characters[choice]['name']
        my_hp = characters[choice]['hp']
        my_damage = characters[choice]['damage']
        break
    else:
        print("Please enter 1, 2, or 3")

# Battle loop
while True:
    # Player's turn
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    
    # Dragon's turn
    my_hp -= dragon_damage
    print(f"The Dragon damaged the {character}!")
    
    if my_hp <= 0:
        print(f"The {character} has lost the battle!")
        break


