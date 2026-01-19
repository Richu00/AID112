n1,n2 = map(int,input("Enter two numbers")).split()
num1,num2 = n1,n2
print(f"Their sum is {num1 + num2},Their difference is {num1 - num2}, Their product is {num1 * num2}")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num2}")
else:
    print(f"{num1} is equal to {num2}")
