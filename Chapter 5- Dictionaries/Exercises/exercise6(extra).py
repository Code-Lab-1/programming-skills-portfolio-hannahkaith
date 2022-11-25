#Exercise 6 
dog = {
    'name' : 'sumo',
    'breed' : 'st. bernard',
    'food' : 'dog food',
    'weight' : '140 pounds'
}
print(dog['name'])
print(dog['breed'])
print(dog.get('weight'))
print(dog.get('height'))
dog.clear()
print(dog)
