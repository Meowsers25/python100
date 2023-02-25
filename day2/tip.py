# Tip Calculator Project
print("Welcome to the tip calculator")

bill_total = float(input("What was the total bill for your meal?\n"))

tip_percentage = int(input("What percentage would you like to tip your waitstaff?\n"))

total_bill = (tip_percentage / 100) * bill_total + bill_total

# print(total_bill)
people = int(input("How many people to split the bill?\n"))

price_per = total_bill / people

final_adjusted = "{:.2f}".format(round(price_per))

print(f"Each person has to pay ${final_adjusted}.")

