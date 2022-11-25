# Exercise 5 : No Pastrami 
sandwich_orders = ['pastrami', 'chicken sandwich', 'pastrami','egg sandwich', 'pastrami', 'ham sandwich', 'grilled cheese']
finished_sandwiches = []

print("Oh dear! Unfortunately, we ran out of pastrami for today :(")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I'm currently making your " + sandwich + "!" )
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("Here is your finished " + sandwich + ". Enjoy!")

print("\n")