# Day 2 project Tip Calculator

print("Welcome to the tip calculator")
bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15?"))
people = int(input("Enter how many people are splitting this bill?"))
tip_amount = ((bill * tip)/100)
each_pay = ((bill + tip_amount) / people)
rounded = round(each_pay, 2)
print(f"Each person should pay: {rounded}")
