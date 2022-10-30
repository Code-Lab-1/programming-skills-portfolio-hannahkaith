#hexagon
import turtle
for x in range(6):
    turtle.forward(90)
    turtle.left(300)

#Star
import turtle
for x in range (10):
    turtle.forward(100)
    turtle.right(144)

#turtle
import turtle
circles= 40
radius= 120
angle= 100
for x in range (circles):
  turtle.circle(radius)
  turtle.left(angle)

  #panda
# Draw Ears
# Draw first ear
import turtle

pen = turtle.Turtle()

def ring(col, rad):

    # set the fill
    prn.fillcolor(col)

    # start filling the color
    pen.begin_fill()

    # draw a circle
    pen.circle(rad)

    # Ending the filling of the color
    pen.end_fill()
pen.up()
pen.setpost(-35,95)
pen.down
ring('black', 15)

pen.up()
pen.setpost(35,95)
pen.down
ring('black', 15)

pen.up()
pen.setpost(0,35)
pen.down
ring('white', 40)

pen.up()
pen.setpost(-18,75)
pen.down
ring('black', 8)

# draw second eye
pen.up()
pen.setpost(18,75)
pen.down
ring('black', 8)

# draw eyes white
#draw first eye
pen.up()
pen.setpost(-18,77)
pen.down
ring('white', 4)

#For Loop
# The following lines will print each letters of a word
print("The following lines will print each letters of Apple")
apple = ["A", "p", "p", "l", "e\n"]
for val in apple:
  print(val) 


print("The following lines will print each letters of Banana")
banana = ["B", "a", "n", "a", "n", "a\n"]
for val in banana:
  print(val)

print("The following lines will print each letters of Car")
car = ["C", "a", "r\n"]
for val in car:
  print(val)

print("The following lines will print each letters of Dolphin")
dolphin = ["D", "o", "l", "p", "h", "i", "n\n"]
for val in dolphin:
  print(val)
  
#For Loop
words =["Apple", "Banana", "Car","Dolphin"]
for word in words:
  #this loop is fteching the word from the list
  print ("The following lines will print each letters of"+word)
  for letter in word:
    #this loop is fetchig letter for the word
    print(letter)
    print("") #this adds a blank space