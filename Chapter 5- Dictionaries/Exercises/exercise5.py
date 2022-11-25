# Exercise 5: Pets
pets = []
pet = {
    'owner' : 'basil',
    'animal' : 'cow',
    'name' : 'kelly',
    'color' : 'brown',
    'gender' : 'male',
    'diet' : 'grass'
}
pets.append(pet)

pet = {
    'owner' : 'omori',
    'animal' : 'cat',
    'name' : 'granola',
    'color' : 'ginger',
    'gender' : 'male',
    'diet' : 'tuna'
}
pets.append(pet)

pet = {
    'owner' : 'alliana',
    'animal' : 'rabbit',
    'name' : 'daisy',
    'color' : 'white',
    'gender' : 'female',
    'diet' : 'carrots'


}
pets.append(pet)

for pet in pets:
    print("\n This is " + pet['name'].title() + "  and their description based on what I know!" )
    for key, value in pet.items():
        print("\t" + key.title() + " -> " + value.title() + ' ✻')
