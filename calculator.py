operator = input("Enter an operator (+ - x /): ")
num1 = float(input("Enter the 1st number jackass: "))
num2 = float(input("Enter the 2nd number, there always need to be a fucking 2nd num: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "x":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator you little ass hole")