print("Welcome to the tip calculator!")

bill = float(input("What was th total bill? $"))
tip = int(input("How much tip you want to pay? 10 12 15 "))
people = int(input("How many people to split the people? "))

bill_with_tip = tip / 100 * bill + bill
#bill_with_tip = bill * (1 + tip / 100)
print(bill_with_tip)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: {final_amount} $")
