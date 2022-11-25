#Exercise 5 : USB Shopper
money = 50
price = 6

usb_sticks = int(money / price)
print("She'll receive {0} USB sticks.".format(usb_sticks))

change = money - (usb_sticks * price)
print("Her change will be {0}.".format(change))

