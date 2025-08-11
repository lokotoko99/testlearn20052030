

product = "Plushie"
unit_price = 4.99
taxable = False
# Sales tax rate value depends on taxable status
if taxable:
    sales_tax_rate = 0.065
else:
    sales_tax_rate = 0
print(sales_tax_rate)
      
# Ternary Operations or Conditional expressions

product = "Plushie"
unit_price = 4.99
taxable = False


# Sales tax rate value depends on taxable status
#Ternary Operations

sales_tax_rate = 0.065 if taxable else 0
print(sales_tax_rate)