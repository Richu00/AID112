
light = input("Enter the colour of the traffic light").lower().strip()
if light == "red":
    print("STOP!")
elif light == "yellow":
    print("Prepare to stop")
elif light == "green":
    print("You can go")
else:
    print("Wrong input")
    
