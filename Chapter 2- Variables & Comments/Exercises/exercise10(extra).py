#Exercise 10
z = int(input("Input the value of z here -> " ))
w = int(input("Input the value of w here -> " ))

temp = z
z = w
w = temp

print("\n")
print('After swapping, the value of z is now: ', z)
print('After swapping, the value of w is now: ', w)