weight = int(input("weight:"))
unit = input("K or Lb:")

if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs:" + str(converted))

else:
    converted = weight * 0.45
    print("weight in Kg:" + str(converted))
