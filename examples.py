temperature = int(input("user: "))

if temperature < -50 and temperature >60:
    print("invalid")
elif temperature >= -50 and temperature <0:
    print("Freezing")
elif temperature >1 and temperature <=15:
    print("User is cold")
elif temperature > 16 and temperature <=25:
    print("User is warm")
elif temperature > 26 and temperature <=35:
    print("User is hot")
elif temperature >36 and temperature <=60:
    print("User is extremly hot")
else:
    print("hot")