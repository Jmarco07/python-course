print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_tip = int(input("How many people to split the bill? "))
tip_percentage = tip / 100
total_tip = total_bill * tip_percentage
total_bill_with_tip = total_bill + total_tip
each_person_bill = round((total_bill_with_tip / split_tip), 2)

print(f"Each person should pay: ${each_person_bill}")