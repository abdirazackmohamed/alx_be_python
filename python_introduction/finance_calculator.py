Monthly_Income = input("Enter your monthly income : ")
Monthly_Income = int(Monthly_Income)
Total_Monthly_Expense = input("Enter your total monthly expenses : ")
Total_Monthly_Expense = int(Total_Monthly_Expense)
Monthly_savings = Monthly_Income - Total_Monthly_Expense
projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Your monthly savings are $", Monthly_savings)
print("Projected savings after one year, with interest is : $", projected_savings)