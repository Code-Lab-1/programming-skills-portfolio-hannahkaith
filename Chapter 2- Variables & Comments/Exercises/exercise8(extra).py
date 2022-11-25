#Exercise 8 (Class Activity)
sub1 = input("Enter your Marks for Subject 1: ")
sub2 = input("Enter your Marks for Subject 2: ")
sub3 = input("Enter your Marks for Subject 3: ")
sub4 = input("Enter your Marks for Subject 4: ")
sub5 = input("Enter your Marks for Subject 5: ")

marks_obtained =  sub1 + sub2 + sub3 + sub4 + sub5
total_marks = 500

average = int(marks_obtained) / 5
percentage = int(marks_obtained) / 500 * 100

print("Your Average mark is ", average)
print("Your Percentage is ", percentage)