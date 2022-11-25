#Exercise 2 : Movie Tickets
question = "How old are you? \n"
question += "Please enter 'quit' when you're done! \n"

while True:
    age = input(question)
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("You get a free ticket! Enjoy :D \n")
    elif age < 13:
        print("Your ticket is $10! Enjoy \n")
    elif age > 12:
        print("You ticket is $15! Enjoy \n")
    else:
        break