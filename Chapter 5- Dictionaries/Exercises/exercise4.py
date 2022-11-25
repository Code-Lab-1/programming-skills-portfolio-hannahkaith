# Exercise 4: Rivers
rivers = {
    "amazon" : "nothern south america",
    "yangtze" : "china",
    "ob" : "western siberia"
}
for river, country in rivers.items():
    print("The "+ river.title() + " river can be located in "+ country.title())

print("\n Below are the Rivers listed in the dictionary: ")
for river in rivers.keys():
    print("-> "+ river.title() + " ✻")

print("\n Below are the Countries listed in the dictionary: ")
for country in rivers.values():
    print("-> "+ country.title() + " ✻")