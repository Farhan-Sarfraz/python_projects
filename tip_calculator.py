print("\nWelcome to thw tip calcculator : ")

bill = float(input("what's the total bill is = ??"))
tip_percentage = int(input("what percenatge tip you want to give of total bill 10,12,15  = ??"))
persons = int(input("total person in trip = "))

tip_per = int(tip_percentage) / 100
total_tip = tip_per * bill

total_bill = bill + total_tip

print("total bill is " ,total_bill)

for_each = total_bill / persons

final_amount = round(for_each , 2)

print(f"each persons should pay {final_amount} ")



