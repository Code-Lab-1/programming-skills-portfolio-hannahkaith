#Exercise 9
food = {
    'steak' : 'savory',
    'pudding' : 'sweet',
    'sinigang' : 'sour',
    "bitter gourd" : 'bitter'
}
for key, value in food.items():
    print(key.title() + " > " + value + ' ☾')