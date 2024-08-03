number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        summation = number_1 + number_2
        print(f"The result is : {summation}")
    case "-":
        subtract = number_1 - number_2
        print(f"The result is : {subtract}")
    case "*":
        multiply = number_1 * number_2
        print(f"The result is : {multiply}")
    case "/":
        if number_2 == 0:
            print("can't divide by zero you cunt")
        else:
            divide = number_1 / number_2
            print(f"The result is : {divide}")
    case _:
        print("invalid entry")
