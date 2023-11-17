#Exercise 10 
characters = {
    'asta' : "aspires to be the Wizard King and end the discrimination in their country.",
    'maka' : "wants to turn her weapon partner, Soul Eater, into a death scythe",
    'senku' : "wants to finally go to space",
    'midoriya' : "become the World's Greatest Hero",
    'gon' : "to find his father, Ging, who was a Hunter"

}

print("The following are fictional characters and their dreams !")
for key, value in characters.items():
    print("\t" + key.title() + " -> " + value + ' ☾')