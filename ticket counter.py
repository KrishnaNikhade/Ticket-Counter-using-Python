#ticket counter
# if height greater than 120cm then person can ride
# for payment if age less than 12 then rupees 10
#if age less than or equal to 18 then rupees 15
# else rupees 20
#rollercoaster

print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm?\n"))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is you curent age?\n"))
  if age < 12:
    print("Please pay rupees 10")
  elif age <= 18:
    print("Please pay rupees 15")
  else:
    print("Please pay rupees 20")
else:
  print("Sorry tum nahi ja sakte ho")

 