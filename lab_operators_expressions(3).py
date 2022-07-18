hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
endhour = (hour*60 + mins + dura) // 60
endmins = (hour*60 + mins + dura) % 60
if endhour <= 23:
    print("Your event will end at " + str(endhour) + ":" + str(endmins))
else:
    print("Your event will end at " + str(endhour-24) + ":" + str(endmins))

#print("Your event will end at " + str((hour*60 + mins + dura) //60)+ ":" + str((hour*60 + mins + dura) %60))