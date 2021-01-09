'''
# 1 operations in python

2 + 3
7 - 4
3 * 2
10 % 2
6 / 3    -> 2.0 (always give float)
2 ** 3   -> 2*2*2
10 * 'str'   -> 'strstrstrstrstrstrstrstrstrstr'

# 2 operators precedence -

1. () -> parentheses
2. **  -> exponents
3. * / -> both have same precedence, anyone of the two operators coming 1st in  
          equation will be given priority.
4. + - -> both have same precedence, anyone of the two operators coming 1st in 
          equation will be given priority.
'''

# Example

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")) # string converted to float
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) 
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2) # round-off to 2 decimal places

#If you want the final_amount to always have 2 decimal places.
#e.g. $12 becomes $12.00
# You can do this instead of line 22
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
