# Exercise 1: Pizza Toppings
question = "What toppings would you like? \n"
question += "Please enter 'quit' when you're done! \n"

while True:
    topping = input(question)
    if topping != 'quit':
        print("Perfect choice! I'll add " + topping + " to your pizza. \n")
    else:
        break

