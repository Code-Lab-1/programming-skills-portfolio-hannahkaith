#Exercise 6 : Shrinking Guest List
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

guest_list = ["Asta", "Itadori Yuuji", "Chifuyu Matsuno", "Chigiri Hyoma"]
print("\n")
print("Sorry for the late notice, but unfortunately I can only accommodate two guests due to some inconveniences. \n")

guest = guest_list.pop(3)
print('Dear ', guest, "\n" "While I originally invited you to dinner, I'm now limiting the number of guests I invited. My apologies for the cancellation! Let's schedule another time to see each other.")
print("\n")
guest1 = guest_list.pop(2)
print('Dear ', guest1, "\n" "While I originally invited you to dinner, I'm now limiting the number of guests I invited. My apologies for the cancellation! Let's schedule another time to see each other.")
print("\n")

for guest in guest_list:
  print("Dear ",guest + ",")
  print("I do hope you can attend dinner." "\n")

del(guest_list[0])
del(guest_list[0])
print('An empty guest list: ', guest_list)

