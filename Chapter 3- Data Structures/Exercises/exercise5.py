#Exercise 5 : Change Guest List
guest_list = ["Asta", "Lee Heeseung", "Chifuyu Matsuno", "Chigiri Hyoma"]
for guest in guest_list:
  print("Dear ",guest + ",")
  print("Good Day! The honor of your presence is requested for dinner on the 25th of November!" "\n")
print("Unfortunately, ", guest_list[1] + " is unable to attend due to work matters.")

guest_list = ["Asta", "Lee Heeseung", "Chifuyu Matsuno", "Chigiri Hyoma"]
print("\n")
del(guest_list[1])
guest_list.insert(1, 'Itadori Yuuji')
for guest in guest_list:
  print("Dear ",guest + ",")
  print("Good Day! The honor of your presence is requested for dinner on the 25th of November!" "\n")
