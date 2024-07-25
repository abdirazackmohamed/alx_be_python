a = input("Enter your monthly income : ")
x = int(a)
b = input("Enter your total monthly expenses : ")
y = int(b)
savings = x - y
projected_savings = savings * 12 + (savings * 12 * 0.05)
print("Your monthly savings are $", savings)
print("Projected savings after one year, with interest is : $",projected_savings)