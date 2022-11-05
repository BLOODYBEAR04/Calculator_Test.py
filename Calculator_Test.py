num1 = input("Enter 1st number: ")
oper = input("Enter desired operation(+,-,&,/): ")
num2 = input("Enter 2nd number: ")

if oper == "+":
    result = float(num1) + float(num2)
    print(num1, "+", num2, "=", result)
elif oper == "-":
    result = float(num1) - float(num2)
    print(num1, "-", num2, "=", result)
elif oper == "*":
    result = float(num1) * float(num2)
    print(num1, "*", num2, "=", result)
elif oper == "/":
    result = float(num1) / float(num2)
    print(num1, "/", num2, "=", result)
else:
    print("WRONG SYNTAX")
