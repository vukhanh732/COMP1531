def tax_calculate(income):   
    if income <= 18200:
        return ("Nil")
    elif income > 18200 and income <= 37000:
        return (0.19 * (income - 18200))
    elif income > 37000 and income <= 87000:
        return (3572 + (0.325 * (income - 37000)))
    elif income > 87000 and income <= 180000:
        return (19822 + (0.37 * (income - 87000)))
    else:
        return (54232 + (0.45 * (income - 180000)))

income = float(input("Enter your income: "))
tax = tax_calculate(income)
print("The estimated tax on your income is ${:0,.2f}".format(tax))