Monthly_Income = float(input("Enter your monthly income: "))
Monthly_Expense = float(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_Income - Monthly_Expense
projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Your monthly savings are $", Monthly_savings)
print("Projected savings after one year, with interest is, : $", projected_savings)