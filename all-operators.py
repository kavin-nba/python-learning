# Create a program to use all python operators available
# Source : https://www.tutorialspoint.com/python3/python_basic_operators.html
print("the options are + - * / // ** % == != > < ")
a = int(input("enter no 1:"))
b = int(input("enter no 2:"))
op = input("enter the option:")
if op == "+":
    result = a+b
elif op == "-":
    result = a-b
elif op == "/":
    result = a/b
elif op == "*":
    result = a*b
elif op == "//":
    result = a**b
elif op == "%":
    result = a%b
elif op == "===":
    print("a is equal to b")
elif op == "!=":
    print("a is not equal to b")
elif op == ">":
    print("a is greater than b")
elif op == "<":
    print("a is less than b")
else:
    print("enter an valid operator:")
print(result)