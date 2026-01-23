tempC = int(input("Enter temperature in celcius"))
tempF = (tempC * (9/5)) + 32
print(f"Temp in ferhenheit is {tempF}")
if tempC < 0:
    print("Very cold wear a thick jacket")
elif tempC >= 0 and tempC <= 15:
    print("Cold, wear a jacket")
elif tempC >= 16 and tempC <= 25:
    print("Nice weather")
else:
    print("Hot! stay hydrated")
    