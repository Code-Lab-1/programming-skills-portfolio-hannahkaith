# Exercise 3: Glossary 2 
glossary = {
    "Floats" : " -> used to represent numbers that aren’t integers / whole numbers ✻ ",
    "Python" : " -> high-level programming language, with applications in numerous areas ✻ ",
    "Append Method" : " -> adds an item to the end of an existing list ✻ ",
    "Print" : " -> used to output text ✻ ",
    "List" : " -> used to store items ✻ ",

    "Len" : " -> to get the number of items in a list ✻",
    "While Loop" : " -> used to repeat a block of code multiple times ✻",
    "Insert Method" : " -> allows you to insert a new item at any position in a list ✻ ",
    "Reverse Method" : " -> used to reverse items in a list ✻",
    "For Loop" : " -> used to iterate over a given sequece, such as lists or strings ✻"

}
for term in glossary:
    print('\n')
    print(term + ": " + "\n" + glossary[term])