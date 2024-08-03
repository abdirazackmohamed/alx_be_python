number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        summation = number_1 + number_2
        print(f"sum of the two number is : {summation}")
    case "-":
        subtract = number_1 - number_2
        print(f"subtraction of the two number is : {subtract}")
    case "*":
        multiply = number_1 * number_2
        print(f"multiplication of the two number is : {multiply}")
    case "/":
        if number_2 == 0:
            print("can't divide by zero you cunt")
        else:
            divide = number_1 / number_2
            print(f"division of the two number is : {divide}")
    case _:
        print("invalid entry")
