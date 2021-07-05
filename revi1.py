weight = float(input("WEIGHT: "))
unit = input("kgs or lbs? ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in lbs" + str(converted))
else:
    converted = weight * 0.45
    print("weight in kgs: " + str(converted))  #weight converter