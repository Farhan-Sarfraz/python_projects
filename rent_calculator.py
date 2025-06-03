
print(" ****=== Rent Calculator for the hostel/Flat ****===")

rent = int(input("Enter your flat rent = "))

food = int(input("Enter the food you want to ordered = "))

electricity_spend = int(input("Enter the electricity spend = "))

charge_per_unit = int(input("Enter the charge per unit = "))

water_bill = int(input("Enter the water bill = "))

internet_bill = int(input("Enter the internet total bill = "))

security_purpose = int(input("Enter the security guard expenses = "))


persons = int(input("Enter the persons living into the flat = "))



total_bill = electricity_spend + charge_per_unit

output = (food + rent + total_bill + security_purpose + internet_bill + water_bill) // persons

print("Each person will pay = " , output)