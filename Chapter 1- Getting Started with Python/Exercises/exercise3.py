#Exercise 3 : Print Date and Time
import datetime
print ("The Current Date & Time ↓  ")
now = datetime.datetime.now()
date = now.strftime("%Y:%m:%d")
print("Date -> ", date)

time = now.strftime("%H:%M:%S")
print("time-> ", time)
"\n"

