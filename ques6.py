city=input("Enter your city :")
city=city.upper()
with open("cities.txt","r") as f:
    t=f.read()
    if city in t:
        print("%s in list of cities"%city)
    else:
        print("%s not in list of cities"%city)