# Main Oeprators for Controlling the Action

# Python Comparison Operators for Decision-Making
"""

== equal
!= is not equal to
< is less than
> is greater than
<= is less than or equal to
>= is greater than or equal to

--Python Logical Operators

and : Both are true
or : One or the other is true
not : Is not true
"""
# if condition: do this no matter what
#Make sure you always use two equal signs with no space between (==) to test
#equality. This rule is easy to forget. If you type it incorrectly, the code won’t work
#as expected.

sun = "down"
if sun == "down":
    print("Good night!")
print("i am here")

total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax : ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total          :${total:.2f}")


import datetime as dt

now = dt.datetime.now()
if now.hour <= 12:
    print(now.hour)
    print("Good Morning")
elif now.hour <= 15:
    print(now.hour)
    print(("Good Afternoon"))
else:
    print(now.hour)
    print(("Good Afternoon"))
print("I hope you are doing well")

light_color = "red"
if light_color =="green":
    print("\nGo!")
elif light_color == "red":
    print("\nStop!")
else:
    print("Proceed with caution")
print("This code executes no matter what")

age= 11
if age < 21:
    #If under 21 drink healthy
    beverage = "milk"
elif age >21 and  age < 65:
    #drink tomatoe juice
    beverage = "tomatoe juice"
else:
    #ensure protein shake
    beverage = "ensure protein shake"
print("plesae drink " + beverage)


product = "Plushie"
unit_price = 4.99
taxable = False
# Sales tax rate value depends on taxable status
if taxable:
    sales_tax_rate = 0.065
else:
    sales_tax_rate = 0
print(sales_tax_rate)