
##TEMPERATURE

name=input("NAME OF THE PLACE: ")

def classify_temperature(temp):
    if temp==999:
        return exit
    elif temp<0:
        return(f"{name} is FREEZING COLD, wear Jacket")
    elif temp>=0 and temp<10:
        return(f"{name} is VERY COLD")
    elif temp>=10 and temp<20:
        return(f"{name} is COLD")
    elif temp>=20 and temp<30:
        return(f"{name} is PLEASANT")
    elif temp>=30 and temp<40:
        return(f"{name} is HOT and be hydrated")
    else:
        return(f"{name} is VERY HOT and stay indoor ")
temp=int(input("PLEASE PROVIDE TEMPERATURE OR TYPE 999 TO exit:  "))

print(classify_temperature(temp))









