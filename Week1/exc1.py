
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height in feet:"))
student_status = input("are you a student?")
print(f"My name is {name} and I am {age} years old. My height is {height: .2f} feet")
if student_status.lower() == "yes":
    print("i am a student")
else:
    print("i am not a student")