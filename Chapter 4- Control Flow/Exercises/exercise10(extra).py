#Exercise 10
while True:
    name = input('What\'s Hannah\'s favorite color? \n')
    if name != 'purple':
        continue
    password = input('Yay!\n What\'s her favorite animal? (It is a dog.) \n')
    if password == 'st. bernard':
        break
print("Permission Granted :>")