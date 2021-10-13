print("the options are + - * / // ** % == != > < ")
while True:
    a = int(input('first num: '))
    op = input('operator: ')
    c = int(input('second num: '))
    if op == '+':
        print(a + c)
    elif op == '-':
        print(a - c)
    elif op == '*':
        print(a * c)
    elif op == '/':
        print(a / c)
    elif op == '//':
        print(a // c)
    elif op == '**':
        print(a ** c)
    elif op == '%':
        print(a % c)
    elif op == '==':
        print("num1 is equal to num2")
    elif op == '!=':
        print("num1 is not equal to num2")
    elif op == '>':
        print("num1 is greater than num2")
    elif op == '<':
        print("num1 is is lesser than num2")
    elif op == 'exit':
        print("program exit")
        break
    else:
        print("wrong operator")