Monthly_Income = float(input("Enter your monthly income: "))
Monthly_Expenses = float(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_Income - Monthly_Expenses
projected_savings = Monthly_savings * 12 + float(Monthly_savings * 12 * 0.05)
print("Your monthly savings are $", Monthly_savings)
print("Projected savings after one year, with interest is, : $", projected_savings)