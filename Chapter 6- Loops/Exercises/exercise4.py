#Exercise 4: Deli 
sandwich_orders = ['chicken sandwich', 'egg sandwich', 'ham sandwich', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I'm currently making your " + sandwich + "!" )
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("Here is your finished " + sandwich + ". Enjoy!")

print("\n")



